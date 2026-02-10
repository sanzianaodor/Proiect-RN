import os

# Calea de baza
BASE_DIR = r"C:\Users\sanzi\Desktop\an 3\sem 1\RN\Clasificarea_instrumentelor_muzicale"

# Caile principale
RAW_DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
PROCESSED_DATA_DIR = os.path.join(BASE_DIR, "data", "processed")

# Caile finale
TRAIN_DIR = os.path.join(BASE_DIR, "data", "train")
VAL_DIR = os.path.join(BASE_DIR, "data", "validation")
TEST_DIR = os.path.join(BASE_DIR, "data", "test")

# Parametrii Audio
SAMPLE_RATE = 22050
DURATION = 3
SAMPLES_PER_TRACK = SAMPLE_RATE * DURATION

# Clasele (Numele folderelor din RAW)

CLASSES = ['chitara', 'pian', 'tobe', 'vioara']

# MAPPING PENTRU REDENUMIRE (Aici decidem cum se vor numi fisierele)
# Cheia este numele folderului din raw, Valoarea este prefixul fisierului
RO_LABELS = {
    'guitar': 'chitara',  'chitara': 'chitara',
    'piano': 'pian',      'pian': 'pian',
    'drums': 'tobe',      'tobe': 'tobe',
    'violin': 'vioara',   'vioara': 'vioara'
}