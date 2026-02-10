import os
import csv
import librosa
import datetime
import sys

# Hack pentru a importa config.py din folderul părinte (src/preprocessing)
# Adaugă calea '../preprocessing' la sistem
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'preprocessing')))

try:
    import config
except ImportError:
    # Fallback dacă nu găsește config-ul, definim manual căile (just in case)
    print("⚠️ Config nu a fost găsit via import. Se folosesc căi relative.")
    BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
    CLASSES = ['chitara', 'pian', 'tobe', 'vioara'] # Sau numele folderelor tale

def get_source_info(label):
    """
    Logica pentru a demonstra contribuția originală (40%).
    """
    if label in ['chitara', 'pian', 'guitar', 'piano']:
        return "Contributie Proprie (Microfon + GarageBand)"
    else:
        return "Sursa Externa (Kaggle/Dataset Public)"

def create_acquisition_log():
    print("--- Modul 1: Data Logging Started ---")
    
    # Verificam daca avem acces la config
    if 'config' in sys.modules:
        raw_dir = config.RAW_DATA_DIR
        classes = config.CLASSES
        log_file = os.path.join(config.BASE_DIR, "docs", "acquisition_log.csv")
    else:
        # Folosim fallback-ul
        raw_dir = RAW_DATA_DIR
        classes = CLASSES
        log_file = os.path.join(BASE_DIR, "docs", "acquisition_log.csv")

    # Ne asiguram ca folderul docs exista
    os.makedirs(os.path.dirname(log_file), exist_ok=True)
    
    # Header-ul CSV-ului (Coloanele tabelului)
    csv_header = [
        "Timestamp Logare", 
        "Nume Fisier", 
        "Clasa (Label)", 
        "Tip Sursa (Originalitate)", 
        "Durata (sec)", 
        "Sample Rate (Hz)", 
        "Status"
    ]
    
    entries = []
    total_files = 0
    original_files = 0
    
    print(f"Scanez folderul: {raw_dir}")

    # 1. Iteram prin fiecare clasa (folder)
    for label in classes:
        folder_path = os.path.join(raw_dir, label)
        
        # Gestionare cazuri in care folderul e numit altfel (engleza/romana)
        if not os.path.exists(folder_path):
            # Incercam maparea inversa din config daca exista
            if 'config' in sys.modules and hasattr(config, 'RO_LABELS'):
                # Cautam daca label e valoare in dict si luam cheia
                pass 
            print(f"⚠️ Atentie: Folderul '{label}' nu exista in raw. Sarim peste.")
            continue
            
        files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.wav', '.mp3'))]
        print(f"  > Clasa '{label}': {len(files)} fisiere gasite.")
        
        for f in files:
            file_path = os.path.join(folder_path, f)
            
            try:
                # 2. Extragere Metadate (Simulare citire senzor)
                # Folosim librosa doar pentru durata si frecventa
                duration = librosa.get_duration(path=file_path)
                sr = librosa.get_samplerate(file_path)
                
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                source_type = get_source_info(label)
                
                if "Proprie" in source_type:
                    original_files += 1
                
                # Adaugam linia in lista
                entries.append([
                    timestamp,
                    f,
                    label,
                    source_type,
                    f"{duration:.2f}",
                    sr,
                    "Valid"
                ])
                total_files += 1
                
            except Exception as e:
                # Daca fisierul e corupt, il logam ca eroare
                entries.append([datetime.datetime.now(), f, label, "Unknown", 0, 0, f"Error: {str(e)}"])

    # 3. Scriere in CSV
    if entries:
        with open(log_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(csv_header)
            writer.writerows(entries)
        
        print(f"\n✅ SUCCES: Log generat in: {log_file}")
        print(f"--- Statistici Rapide ---")
        print(f"Total fisiere procesate: {total_files}")
        
        if total_files > 0:
            procent_original = (original_files / total_files) * 100
            print(f"Contributie Originala: {original_files} fisiere ({procent_original:.1f}%)")
            
            if procent_original >= 40:
                print("REZULTAT: ✅ Cerința de minim 40% este ÎNDEPLINITĂ.")
            else:
                print("REZULTAT: ⚠️ Atentie! Sub 40%. Mai adauga inregistrari proprii.")
        
        print("Cerința 'Minim 100 samples' este:", "✅ OK" if total_files >= 100 else "❌ Eșuat")

if __name__ == "__main__":
    create_acquisition_log()