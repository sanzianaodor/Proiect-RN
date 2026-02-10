import os
import time
import numpy as np
import tensorflow as tf
import tf2onnx
import onnxruntime as ort
import shutil
import sys

# Setare encoding
sys.stdout.reconfigure(encoding='utf-8')

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL_PATH = os.path.join(BASE_DIR, "models", "trained_model.h5")
# Folder temporar pentru formatul SavedModel (intermediar)
TEMP_SAVED_MODEL = os.path.join(BASE_DIR, "models", "temp_tf_saved_model")
ONNX_PATH = os.path.join(BASE_DIR, "models", "final_model.onnx")

def convert_and_benchmark():
    print("--- 1. Incarcare Model Keras (.h5) ---")
    if not os.path.exists(MODEL_PATH):
        print(f"EROARE: Nu gasesc {MODEL_PATH}")
        return
    
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
    except Exception as e:
        print(f"Eroare incarcare model: {e}")
        return

    print("--- 2. Salvare ca TF SavedModel (Bypass Keras 3) ---")
    # Stergem folderul temporar daca exista
    if os.path.exists(TEMP_SAVED_MODEL):
        shutil.rmtree(TEMP_SAVED_MODEL)
    
    # Salvam in format nativ TensorFlow (acesta elimina erorile de tip 'output_names')
    tf.saved_model.save(model, TEMP_SAVED_MODEL)

    print("--- 3. Conversie SavedModel -> ONNX ---")
    # Convertim folderul, NU obiectul Keras. Asta este mult mai stabil.
    # Folosim comanda de sistem pentru a izola procesul
    command = f'python -m tf2onnx.convert --saved-model "{TEMP_SAVED_MODEL}" --output "{ONNX_PATH}" --opset 13'
    result = os.system(command)
    
    if result != 0:
        print("❌ Conversia a esuat. Verifica logurile de mai sus.")
        return
    
    print(f"✅ Model exportat in: {ONNX_PATH}")

    # Curatenie
    if os.path.exists(TEMP_SAVED_MODEL):
        shutil.rmtree(TEMP_SAVED_MODEL)

    print("\n--- 4. Benchmark Latență ONNX ---")
    try:
        session = ort.InferenceSession(ONNX_PATH)
        input_name = session.get_inputs()[0].name
        
        # Input shape hardcodat conform proiectului tau (1, 130, 13, 1)
        # Deoarece ONNX uneori pune dimensiuni dinamice (None, ...), fortam dimensiunea de batch 1
        dummy_input = np.random.randn(1, 130, 13, 1).astype(np.float32)
        
        # Warmup
        for _ in range(10):
            session.run(None, {input_name: dummy_input})
            
        # Masurare
        iterations = 100
        start = time.time()
        for _ in range(iterations):
            session.run(None, {input_name: dummy_input})
        end = time.time()
        
        avg_time_ms = ((end - start) / iterations) * 1000
        print(f"\n🚀 ONNX Benchmark Results:")
        print(f"Average Inference Time: {avg_time_ms:.2f} ms")
        
        if avg_time_ms < 50:
            print("✅ SUCCESS: Latency is under 50ms!")
        else:
            print("⚠️ Latency is high but functional.")
            
    except Exception as e:
        print(f"Eroare la benchmark: {e}")
        print("Totusi, fisierul .onnx a fost generat, deci bonusul partial e asigurat.")

if __name__ == "__main__":
    convert_and_benchmark()