import librosa
import numpy as np
import soundfile as sf
import pandas as pd  # Necesită: pip install pandas
import os
import time
from datetime import datetime

# --- CONFIGURAȚIE ---
TARGET_SR = 16000
TARGET_DURATION = 3.0
TARGET_SAMPLES = int(TARGET_SR * TARGET_DURATION)

# Căi relative
BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'data')
RAW_DIR = os.path.join(BASE_DIR, 'raw')
PROCESSED_DIR = os.path.join(BASE_DIR, 'processed')
LOG_FILE = os.path.join(BASE_DIR, 'dataset_metadata.csv')

def process_audio(file_path):
    """
    Aplică transformarea esențială: Denoising + Uniformizare
    Returnează semnalul audio procesat și durata originală.
    """
    try:
        # 1. Încărcare
        y, sr = librosa.load(file_path, sr=TARGET_SR, mono=True)
        orig_duration = librosa.get_duration(y=y, sr=sr)

        # 2. Denoising (Eliminare liniște/zgomot margini)
        y_trimmed, _ = librosa.effects.trim(y, top_db=25)

        # 3. Uniformizare Lungime (Padding/Trunchiere)
        if len(y_trimmed) > TARGET_SAMPLES:
            y_final = y_trimmed[:TARGET_SAMPLES]
        else:
            padding = TARGET_SAMPLES - len(y_trimmed)
            y_final = np.pad(y_trimmed, (0, padding), 'constant')

        # 4. Normalizare
        if np.max(np.abs(y_final)) > 0:
            y_final = y_final / np.max(np.abs(y_final))

        return y_final, orig_duration
    except Exception as e:
        print(f"Eroare procesare {file_path}: {e}")
        return None, 0

def main():
    print("--- Modul 1: Data Logging & Acquisition ---")
    print(f"Sursă: {RAW_DIR}")
    print(f"Destinație: {PROCESSED_DIR}")
    
    # Creare foldere destinație
    if not os.path.exists(PROCESSED_DIR):
        os.makedirs(PROCESSED_DIR)

    data_log = [] # Lista pentru stocarea datelor din CSV
    
    # Iterare prin clase
    classes = [d for d in os.listdir(RAW_DIR) if os.path.isdir(os.path.join(RAW_DIR, d))]
    
    for label in classes:
        class_raw_path = os.path.join(RAW_DIR, label)
        class_proc_path = os.path.join(PROCESSED_DIR, label)
        os.makedirs(class_proc_path, exist_ok=True)
        
        files = [f for f in os.listdir(class_raw_path) if f.endswith(('.wav', '.mp3'))]
        
        print(f"Procesare clasa '{label}': {len(files)} fișiere găsite.")
        
        for filename in files:
            raw_file_path = os.path.join(class_raw_path, filename)
            
            # --- ACQUISITION & PROCESSING ---
            start_time = time.time()
            audio_data, orig_dur = process_audio(raw_file_path)
            proc_time = time.time() - start_time
            
            if audio_data is not None:
                # Salvare fișier procesat
                processed_filename = f"proc_{filename}"
                processed_file_path = os.path.join(class_proc_path, processed_filename)
                sf.write(processed_file_path, audio_data, TARGET_SR)
                
                # --- DATA LOGGING (Generare rând CSV) ---
                log_entry = {
                    'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    'filename': processed_filename,
                    'original_file': filename,
                    'label': label,
                    'sampling_rate': TARGET_SR,
                    'duration_sec': TARGET_DURATION,
                    'original_duration': round(orig_dur, 2),
                    'processing_time_ms': round(proc_time * 1000, 2),
                    'status': 'Acquired_Clean',
                    'file_path': processed_file_path
                }
                data_log.append(log_entry)

    # Salvare CSV Final
    df = pd.DataFrame(data_log)
    df.to_csv(LOG_FILE, index=False)
    
    print("-" * 30)
    print(f"Succes! Au fost procesate {len(df)} fișiere.")
    print(f"Jurnalul de date (CSV) a fost generat: {LOG_FILE}")
    print("Modulul Data Acquisition a rulat complet.")

if __name__ == "__main__":
    main()