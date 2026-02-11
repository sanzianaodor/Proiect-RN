import sys
import os
import json
import warnings
import numpy as np
import librosa
import tensorflow as tf
import pickle

# --- MODIFICARE DEBUG ---
debug_file = r"C:\Clasificarea_instrumentelor_muzicale\debug_log.txt"
with open(debug_file, "w") as f:
    f.write(f"Python a pornit! Argv: {sys.argv}\n")
# ------------------------
# ---------------- SETUP ----------------
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
warnings.filterwarnings('ignore')
sys.stdout.reconfigure(encoding='utf-8')

SAMPLE_RATE = 22050
DURATION = 3
N_MFCC = 13
MAX_LEN = 130
THRESHOLD = 0.60

# ---------------- PATHS ----------------
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, '..', '..'))

DATA_ROOT = os.path.join(PROJECT_ROOT, "data")
MODEL_PATH = r"C:\Clasificarea_instrumentelor_muzicale\models\optimized_model.h5"
SCALER_PATH = os.path.join(PROJECT_ROOT, "config", "preprocessing_params.pkl")
CLASSES_PATH = os.path.join(PROJECT_ROOT, "config", "classes.npy")

# ---------------- UTILS ----------------
def find_file_in_data(filename):
    for root, dirs, files in os.walk(DATA_ROOT):
        if filename in files:
            return os.path.join(root, filename)
    return None

def load_artifacts():
    model = tf.keras.models.load_model(MODEL_PATH)
    scaler = None
    if os.path.exists(SCALER_PATH):
        with open(SCALER_PATH, 'rb') as f:
            scaler = pickle.load(f)
    classes = np.load(CLASSES_PATH, allow_pickle=True)
    return model, scaler, classes

def preprocess_audio(file_path, scaler):
    y, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
    expected_len = SAMPLE_RATE * DURATION
    if len(y) < expected_len:
        y = np.pad(y, (0, expected_len - len(y)))
    else:
        y = y[:expected_len]

    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
    mfcc = mfcc[:, :MAX_LEN] if mfcc.shape[1] > MAX_LEN else np.pad(
        mfcc, ((0, 0), (0, MAX_LEN - mfcc.shape[1]))
    )

    mfcc = mfcc.T
    if scaler:
        mfcc = scaler.transform(mfcc)

    return mfcc.reshape(1, MAX_LEN, N_MFCC, 1)

# ---------------- MAIN LOGIC ----------------
def predict(filename):
    filename = filename.strip('"').strip("'")

    full_path = None
    if os.path.isfile(filename):
        full_path = filename
    else:
        full_path = find_file_in_data(filename)

    if not full_path:
        print(json.dumps({"instrument": "ERROR: FILE NOT FOUND", "confidence": 0}))
        return

    model, scaler, classes = load_artifacts()
    X = preprocess_audio(full_path, scaler)

    preds = model.predict(X, verbose=0)[0]
    idx = int(np.argmax(preds))
    conf = float(preds[idx])
    label = str(classes[idx])

    if conf < THRESHOLD:
        label = "UNCERTAIN"

    print(json.dumps({
        "instrument": label,
        "confidence": f"{conf:.4f}"
    }))
   

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(json.dumps({"instrument": "ERROR: NO ARG", "confidence": 0}))
    else:
        predict(sys.argv[1])
