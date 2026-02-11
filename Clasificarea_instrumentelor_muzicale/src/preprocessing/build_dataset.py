import os
import shutil
import config
import utils
from sklearn.model_selection import train_test_split

def step_1_clean_and_rename():
    """
    PASUL 1: Ia tot din RAW, uniformizeaza, REDENUMESTE (chitara_1, chitara_2...)
    si salveaza in PROCESSED.
    """
    print(f"\n--- PASUL 1: Curatare, Redenumire si Uniformizare ---")
    
    if os.path.exists(config.PROCESSED_DATA_DIR):
        shutil.rmtree(config.PROCESSED_DATA_DIR)
    
    for label in config.CLASSES:
        raw_folder = os.path.join(config.RAW_DATA_DIR, label)
        processed_folder = os.path.join(config.PROCESSED_DATA_DIR, label)
        
        if not os.path.exists(raw_folder):
            print(f"ATENTIE: Folderul '{raw_folder}' nu exista! Verifica config.CLASSES.")
            continue

        files = [f for f in os.listdir(raw_folder) if f.endswith('.wav') or f.endswith('.mp3')]
        print(f" > Procesez clasa '{label}': {len(files)} fisiere...")
        
        nume_romanesc = config.RO_LABELS.get(label, label)
        
        count_saved = 0
        for index, f in enumerate(files, start=1):
            file_path = os.path.join(raw_folder, f)
            signal = utils.load_and_fix_length(file_path)
            
            if signal is not None:
                save_name = f"{nume_romanesc}_{index}.wav"
                utils.save_audio(signal, processed_folder, save_name)
                count_saved += 1
                
        print(f"   Salvat: {count_saved} fisiere ca {nume_romanesc}_X.wav")

def step_2_split_no_augment():
    """
    PASUL 2: Imparte in Train (70%), Val (15%), Test (15%).
    FARA AUGMENTARE (augment=False peste tot).
    """
    print("\n--- PASUL 2: Impartire (70/15/15) - FARA AUGMENTARE ---")
    
    # Curatam folderele finale
    for d in [config.TRAIN_DIR, config.VAL_DIR, config.TEST_DIR]:
        if os.path.exists(d): shutil.rmtree(d)

    for label in config.CLASSES:
        source_folder = os.path.join(config.PROCESSED_DATA_DIR, label)
        
        if not os.path.exists(source_folder): continue

        files = [f for f in os.listdir(source_folder) if f.endswith('.wav')]
        
        # Impartire matematica
        # 80 fisiere -> Train: 56, Val: 12, Test: 12
        train_files, test_files = train_test_split(files, test_size=0.3, random_state=42)
        val_files, test_files = train_test_split(test_files, test_size=0.5, random_state=42)
        
        def process_subset(file_list, destination_root, augment=False):
            dest_folder = os.path.join(destination_root, label)
            os.makedirs(dest_folder, exist_ok=True)
            
            for filename in file_list:
                src_path = os.path.join(source_folder, filename)
                
                # 1. Copiem originalul
                shutil.copy(src_path, os.path.join(dest_folder, filename))
                
                # 2. Augmentam DOAR daca augment=True (acum e setat pe False)
                if augment:
                    signal = utils.load_and_fix_length(src_path)
                    utils.save_audio(utils.add_noise(signal), dest_folder, filename.replace('.wav', '_noise.wav'))
                    utils.save_audio(utils.change_pitch(signal, 2), dest_folder, filename.replace('.wav', '_pUp.wav'))
                    utils.save_audio(utils.change_pitch(signal, -2), dest_folder, filename.replace('.wav', '_pDown.wav'))

        
        process_subset(train_files, config.TRAIN_DIR, augment=False)
        process_subset(val_files, config.VAL_DIR, augment=False)
        process_subset(test_files, config.TEST_DIR, augment=False)
        
        print(f" Clasa '{label}': Train={len(train_files)}, Val={len(val_files)}, Test={len(test_files)}")

if __name__ == "__main__":
    step_1_clean_and_rename()
    step_2_split_no_augment()
    print("\n--- GATA! Fisiere impartite exact 70-15-15. ---")
