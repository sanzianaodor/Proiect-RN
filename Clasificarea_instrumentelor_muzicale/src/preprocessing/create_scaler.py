import os
import numpy as np
import librosa
import pickle
from sklearn.preprocessing import StandardScaler
import sys

# Configurare encoding
sys.stdout.reconfigure(encoding='utf-8')

# Cai
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
CONFIG_DIR = os.path.join(BASE_DIR, "config")
SCALER_PATH = os.path.join(CONFIG_DIR, "preprocessing_params.pkl")

# Parametri Audio (Aceiasi ca peste tot)
SAMPLE_RATE = 22050
DURATION = 3
N_MFCC = 13
MAX_LEN = 130 

def extract_features_flat(file_path):
    """Extragem MFCC dar le returnam ca lista de frame-uri pentru scaler"""
    try:
        y, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
        # Pad/Trim
        expected_samples = int(SAMPLE_RATE * DURATION)
        if len(y) < expected_samples:
            y = np.pad(y, (0, expected_samples - len(y)))
        else:
            y = y[:expected_samples]
            
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
        
        # Transpunem: (13, Time) -> (Time, 13)
        # Scalerul vrea (Exemple, Features)
        return mfcc.T 
    except:
        return None

def main():
    print("--- Generare Scaler (StandardScaler) ---")
    
    # Ne asiguram ca folderul config exista
    os.makedirs(CONFIG_DIR, exist_ok=True)
    
    all_features = []
    
    # Parcurgem datele
    classes = [d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))]
    
    print("Colectare date pentru statistici...")
    for label in classes:
        folder = os.path.join(DATA_DIR, label)
        for fname in os.listdir(folder):
            if fname.endswith('.wav'):
                path = os.path.join(folder, fname)
                feats = extract_features_flat(path)
                if feats is not None:
                    # Adaugam toate frame-urile in lista mare
                    all_features.append(feats)

    # Concatenam totul intr-o matrice gigantica (Total_Frames x 13)
    # Asta ne permite sa calculam media globala per coeficient MFCC
    X_all = np.vstack(all_features)
    print(f"Dataset pentru scalare: {X_all.shape}")
    
    # Fit Scaler
    scaler = StandardScaler()
    scaler.fit(X_all)
    
    # Salvare
    with open(SCALER_PATH, 'wb') as f:
        pickle.dump(scaler, f)
        
    print(f"✅ Scaler salvat cu succes in: {SCALER_PATH}")
    print("⚠️  IMPORTANT: Acum trebuie sa re-rulezi antrenarea (train_enhanced.py)!")

if __name__ == "__main__":
    main()