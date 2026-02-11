import os
import glob
import pandas as pd
import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import config 

# Ne asiguram ca folderul de documentatie exista
DOCS_DIR = os.path.join(config.BASE_DIR, "docs", "datasets")
os.makedirs(DOCS_DIR, exist_ok=True)

def generate_statistics_csv():
    print("--- Generare Tabel Statistici ---")
    
    data = []
    sets = {
        "Train": config.TRAIN_DIR,
        "Validation": config.VAL_DIR,
        "Test": config.TEST_DIR
    }
    
    # Numaram fisierele
    for subset_name, subset_path in sets.items():
        if not os.path.exists(subset_path):
            continue
            
        for label in config.CLASSES:
            folder_path = os.path.join(subset_path, label)
            if os.path.exists(folder_path):
                # Numaram wav-urile
                count = len(glob.glob(os.path.join(folder_path, "*.wav")))
                data.append({
                    "Set Date": subset_name,
                    "Clasa (Instrument)": label,
                    "Numar Fisiere": count
                })
    
    # Cream tabelul
    df = pd.DataFrame(data)
    
    # Calculam totaluri
    if not df.empty:
        total_files = df["Numar Fisiere"].sum()
        print(f"Total fisiere gasite: {total_files}")
        
        # Salvam CSV
        csv_path = os.path.join(DOCS_DIR, "data_stats.csv")
        df.to_csv(csv_path, index=False)
        print(f"✅ Tabel salvat in: {csv_path}")
    else:
        print("⚠️ Nu s-au gasit fisiere. Verifica daca ai rulat build_dataset.py")

def plot_comparison(file_path_1, name_1, file_path_2, name_2):
    print(f"--- Generare Grafic Comparativ: {name_1} vs {name_2} ---")
    
    try:
        # Incarcam fisierele
        y1, sr = librosa.load(file_path_1, sr=config.SAMPLE_RATE)
        y2, _ = librosa.load(file_path_2, sr=config.SAMPLE_RATE)
        
        # Configuram imaginea (2 coloane, 2 randuri)
        fig, ax = plt.subplots(2, 2, figsize=(12, 8))
        fig.suptitle('Comparatie Semnal Audio: Diferențe între Clase', fontsize=16)

        # --- PLOT 1: Waveform (Forma de unda) ---
        librosa.display.waveshow(y1, sr=sr, ax=ax[0, 0], alpha=0.8, color="blue")
        ax[0, 0].set_title(f'Waveform: {name_1}')
        ax[0, 0].set_xlabel("Timp (s)")
        ax[0, 0].set_ylabel("Amplitudine")
        ax[0, 0].grid(True, alpha=0.3)

        librosa.display.waveshow(y2, sr=sr, ax=ax[0, 1], alpha=0.8, color="orange")
        ax[0, 1].set_title(f'Waveform: {name_2}')
        ax[0, 1].set_xlabel("Timp (s)")
        ax[0, 1].grid(True, alpha=0.3)

        # --- PLOT 2: Spectrograma (Amprenta vocala) ---
        D1 = librosa.amplitude_to_db(np.abs(librosa.stft(y1)), ref=np.max)
        D2 = librosa.amplitude_to_db(np.abs(librosa.stft(y2)), ref=np.max)

        img1 = librosa.display.specshow(D1, sr=sr, x_axis='time', y_axis='log', ax=ax[1, 0])
        ax[1, 0].set_title(f'Spectrogramă: {name_1}')
        fig.colorbar(img1, ax=ax[1, 0], format="%+2.0f dB")

        img2 = librosa.display.specshow(D2, sr=sr, x_axis='time', y_axis='log', ax=ax[1, 1])
        ax[1, 1].set_title(f'Spectrogramă: {name_2}')
        fig.colorbar(img2, ax=ax[1, 1], format="%+2.0f dB")

        plt.tight_layout()
        
        # Salvam imaginea
        img_path = os.path.join(DOCS_DIR, "waveform_comparison.png")
        plt.savefig(img_path, dpi=150)
        print(f"✅ Grafic salvat in: {img_path}")
        plt.close()
    except Exception as e:
        print(f"Eroare la generarea graficului: {e}")

def main():
    # 1. Generam CSV-ul
    generate_statistics_csv()
    
    # 2. Cautam 2 fisiere de test pentru grafic
    # Luam primele 2 clase din lista
    clasa_1 = config.CLASSES[0] 
    clasa_2 = config.CLASSES[2] 
    
    path_1 = glob.glob(os.path.join(config.TRAIN_DIR, clasa_1, "*.wav"))
    path_2 = glob.glob(os.path.join(config.TRAIN_DIR, clasa_2, "*.wav"))
    
    if path_1 and path_2:
        # Folosim numele romanesc daca exista in dictionar, altfel numele folderului
        nume_1 = config.RO_LABELS.get(clasa_1, clasa_1).capitalize()
        nume_2 = config.RO_LABELS.get(clasa_2, clasa_2).capitalize()
        
        plot_comparison(path_1[0], nume_1, 
                        path_2[0], nume_2)
    else:
        print(" Nu am gasit fisiere suficiente pentru grafic.")
        print(f"Am cautat in: {os.path.join(config.TRAIN_DIR, clasa_1)} si {clasa_2}")

if __name__ == "__main__":
    main()
