import librosa
import numpy as np
import soundfile as sf
import os

# --- PARAMETRI DE PROCESARE ---
TARGET_SR = 16000          # Frecvența de eșantionare țintă (Hz)
TARGET_DURATION = 3.0      # Durata fixă țintă (secunde)
BASE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '..', 'data')

INPUT_DIR = os.path.join(BASE_DIR, 'raw')
OUTPUT_DIR = os.path.join(BASE_DIR, 'processed')

TARGET_N_SAMPLES = int(TARGET_DURATION * TARGET_SR)


def process_audio_file(file_path, output_sub_dir):
    """
    Încarcă, reeșantionează, ajustează lungimea și salvează un fișier audio.
    """
    try:
        # 1. Încărcare și reeșantionare (uniformizare frecvență)
        audio, sr = librosa.load(file_path, sr=TARGET_SR, mono=True)
        current_length = len(audio)

        # 2. Ajustarea Lungimii (uniformizare lungime)
        if current_length > TARGET_N_SAMPLES:
            # Trunchiere
            audio = audio[:TARGET_N_SAMPLES]
        elif current_length < TARGET_N_SAMPLES:
            # Padding
            padding_needed = TARGET_N_SAMPLES - current_length
            audio = np.pad(audio, (0, padding_needed), 'constant')

        # 3. Salvarea fișierului procesat
        
        # Asigură-te că folderul de clasă (ex: pian) există în 'processed'
        final_output_dir = os.path.join(OUTPUT_DIR, output_sub_dir)
        os.makedirs(final_output_dir, exist_ok=True)
        
        output_filename = os.path.join(final_output_dir, os.path.basename(file_path))
        sf.write(output_filename, audio, TARGET_SR)
        
        print(f"[SUCCES] Procesat: {output_sub_dir}/{os.path.basename(file_path)}")
        return True

    except Exception as e:
        print(f"[EROARE] Nu s-a putut procesa {file_path}: {e}")
        return False

def main():
    print(f"--- Începe Preprocesarea ---")
    print(f"Sursă: {INPUT_DIR}")
    print(f"Destinație: {OUTPUT_DIR}")
    print("-" * 30)

    processed_count = 0
    
    # Parcurge folderele de clasă (pian, vioara, chitara, tobe)
    for class_name in os.listdir(INPUT_DIR):
        class_path = os.path.join(INPUT_DIR, class_name)
        
        # Asigură-te că este un folder
        if os.path.isdir(class_path):
            print(f"\n--- Procesare Clasă: {class_name.upper()} ---")
            
            # Parcurge fișierele din folderul clasei
            for filename in os.listdir(class_path):
                if filename.lower().endswith(('.wav', '.mp3', '.flac')):
                    file_path = os.path.join(class_path, filename)
                    
                    if process_audio_file(file_path, class_name):
                        processed_count += 1
    
    print("-" * 30)
    print(f"--- Procesare Finalizată ---")
    print(f"Total fișiere procesate și uniformizate: {processed_count}")

if __name__ == "__main__":
    main()