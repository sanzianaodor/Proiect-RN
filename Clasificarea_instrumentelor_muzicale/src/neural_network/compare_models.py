import os
import numpy as np
import tensorflow as tf
from tensorflow.keras import layers, models # type: ignore
import librosa
import time
import sys

# Setam encoding pentru consola
sys.stdout.reconfigure(encoding='utf-8')

# --- CONFIGURARE ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw") 

# Parametri audio (trebuie sa fie IDENTICI cu cei din antrenare)
SAMPLE_RATE = 22050
DURATION = 3 
N_MFCC = 13
MAX_LEN = 130 

def extract_features(file_path):
    """Functie locala de extragere MFCC"""
    try:
        y, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
        expected_samples = int(SAMPLE_RATE * DURATION)
        if len(y) < expected_samples:
            y = np.pad(y, (0, expected_samples - len(y)))
        else:
            y = y[:expected_samples]
            
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
        
        if mfcc.shape[1] > MAX_LEN:
            mfcc = mfcc[:, :MAX_LEN]
        else:
            mfcc = np.pad(mfcc, ((0, 0), (0, MAX_LEN - mfcc.shape[1])))
            
        return mfcc.T
    except Exception as e:
        print(f"Eroare fisier: {e}")
        return None

def load_dataset():
    """Incarca datele pentru comparatie"""
    X = []
    y = []
    classes = sorted([d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))])
    
    print(f"Clase gasite: {classes}")
    
    for idx, label in enumerate(classes):
        folder_path = os.path.join(DATA_DIR, label)
        files = [f for f in os.listdir(folder_path) if f.endswith('.wav')]
        
        # Luam doar primele 50 fisiere per clasa pentru viteza la comparatie
        # (Nu e nevoie sa antrenam pe tot datasetul pentru acest bonus)
        for file_name in files[:50]: 
            path = os.path.join(folder_path, file_name)
            feature = extract_features(path)
            if feature is not None:
                X.append(feature)
                y.append(idx)
                
    return np.array(X), np.array(y), classes

def build_mlp_model(input_shape, num_classes):
    """Arhitectura MLP (Simpla - Doar Dense)"""
    model = models.Sequential([
        layers.Flatten(input_shape=input_shape),
        layers.Dense(256, activation='relu'),
        layers.Dropout(0.3),
        layers.Dense(128, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def build_cnn_model(input_shape, num_classes):
    """Arhitectura CNN (Complexa - Convolutii)"""
    model = models.Sequential([
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        layers.MaxPooling2D((2, 2)),
        layers.Conv2D(64, (3, 3), activation='relu'),
        layers.MaxPooling2D((2, 2)),
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model

def main():
    print("--- 1. Incarcare Date (Subset rapid) ---")
    X, y, classes = load_dataset()
    
    if len(X) == 0:
        print("EROARE: Nu am gasit date! Verifica folderul data/raw")
        return

    # Reshape pentru retea: (Batch, 130, 13, 1)
    X = X.reshape(X.shape[0], MAX_LEN, N_MFCC, 1)
    print(f"Date incarcate: {X.shape}")
    
    # --- 2. Antrenare CNN ---
    print("\n--- Antrenare Model A: CNN ---")
    cnn = build_cnn_model((MAX_LEN, N_MFCC, 1), len(classes))
    start_cnn = time.time()
    # Antrenam putin (10 epoci) doar cat sa vedem trendul
    hist_cnn = cnn.fit(X, y, epochs=15, batch_size=16, verbose=0, validation_split=0.2)
    time_cnn = time.time() - start_cnn
    acc_cnn = max(hist_cnn.history['val_accuracy'])
    
    # --- 3. Antrenare MLP ---
    print("\n--- Antrenare Model B: MLP (Simplu) ---")
    mlp = build_mlp_model((MAX_LEN, N_MFCC, 1), len(classes))
    start_mlp = time.time()
    hist_mlp = mlp.fit(X, y, epochs=15, batch_size=16, verbose=0, validation_split=0.2)
    time_mlp = time.time() - start_mlp
    acc_mlp = max(hist_mlp.history['val_accuracy'])

    # --- 4. Raport Final ---
    print("\n" + "="*40)
    print("      REZULTATE COMPARATIVE")
    print("="*40)
    print(f"METRICA        | CNN (Ales) | MLP (Simplu)")
    print("-" * 40)
    print(f"Acuratete Max  | {acc_cnn*100:.2f}%     | {acc_mlp*100:.2f}%")
    print(f"Timp Antrenare | {time_cnn:.2f}s      | {time_mlp:.2f}s")
    print(f"Nr. Parametri  | {cnn.count_params()}     | {mlp.count_params()}")
    print("-" * 40)
    
    if acc_cnn > acc_mlp:
        print("CONCLUZIE: CNN este superior pentru spectrograma.")
    else:
        print("CONCLUZIE: Datele sunt insuficiente pentru a diferentia clar.")

if __name__ == "__main__":
    main()