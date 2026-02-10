import os
import numpy as np
import librosa
import tensorflow as tf
import pickle
import pandas as pd  # <--- NOU: Pentru salvare CSV
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Setare encoding
sys.stdout.reconfigure(encoding='utf-8')

# --- CONFIGURARE ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DATA_DIR = os.path.join(BASE_DIR, "data", "raw")
MODELS_DIR = os.path.join(BASE_DIR, "models")
DOCS_DIR = os.path.join(BASE_DIR, "docs")
RESULTS_DIR = os.path.join(BASE_DIR, "results")  # <--- NOU: Folder rezultate
SCALER_PATH = os.path.join(BASE_DIR, "config", "preprocessing_params.pkl")

# Creare foldere necesare
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(DOCS_DIR, exist_ok=True)
os.makedirs(RESULTS_DIR, exist_ok=True)

# Parametri
SAMPLE_RATE = 22050
DURATION = 3
N_MFCC = 13
MAX_LEN = 130 
BATCH_SIZE = 16
EPOCHS = 50       
LEARNING_RATE = 0.001

# Importam arhitectura
from model import build_cnn_model

def load_scaler():
    """Incarca scalerul salvat anterior"""
    if not os.path.exists(SCALER_PATH):
        raise FileNotFoundError(f"Nu gasesc scalerul la {SCALER_PATH}. Ruleaza create_scaler.py!")
    with open(SCALER_PATH, 'rb') as f:
        return pickle.load(f)

def extract_features_scaled(file_path, scaler):
    """Extrage si SCALEAZA datele"""
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
            
        # Scalare
        mfcc_T = mfcc.T 
        mfcc_scaled = scaler.transform(mfcc_T)
        
        return mfcc_scaled
    except Exception as e:
        print(f"Eroare procesare {file_path}: {e}")
        return None

def augment_data(X_train, y_train):
    """Adauga zgomot pentru a dubla datele"""
    noise = np.random.randn(*X_train.shape) * 0.005
    X_augmented = X_train + noise
    return np.concatenate((X_train, X_augmented), axis=0), np.concatenate((y_train, y_train), axis=0)

def save_training_history(history):
    """Salveaza istoricul (loss/acc) in CSV pentru verificare"""
    hist_df = pd.DataFrame(history.history)
    hist_df.index.name = 'epoch'
    csv_path = os.path.join(RESULTS_DIR, "training_history.csv")
    hist_df.to_csv(csv_path)
    print(f"✅ Istoric antrenare salvat in: {csv_path}")

def plot_training_results(history, y_true, y_pred, class_names):
    # Grafice Loss/Accuracy
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']
    loss = history.history['loss']
    val_loss = history.history['val_loss']
    epochs_range = range(len(acc))

    plt.figure(figsize=(16, 6))
    plt.subplot(1, 2, 1)
    plt.plot(epochs_range, loss, label='Train Loss')
    plt.plot(epochs_range, val_loss, label='Val Loss')
    plt.legend()
    plt.title('Loss Curve')

    plt.subplot(1, 2, 2)
    plt.plot(epochs_range, acc, label='Train Acc')
    plt.plot(epochs_range, val_acc, label='Val Acc')
    plt.legend()
    plt.title('Accuracy Curve')
    plt.savefig(os.path.join(DOCS_DIR, "loss_curve.png"))
    
    # Matrice Confuzie
    plt.figure(figsize=(8, 6))
    cm = confusion_matrix(y_true, y_pred)
    sns.heatmap(cm, annot=True, fmt='d', xticklabels=class_names, yticklabels=class_names)
    plt.savefig(os.path.join(DOCS_DIR, "confusion_matrix.png"))

def main():
    print("--- Pornire Pipeline Antrenare ---")
    
    # 1. Incarcare Scaler
    scaler = load_scaler()
    
    # 2. Incarcare Date
    X = []
    y = []
    classes = sorted([d for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d))])
    
    print(f"Clase identificate: {classes}")
    
    for idx, label in enumerate(classes):
        folder_path = os.path.join(DATA_DIR, label)
        for fname in os.listdir(folder_path):
            if fname.endswith('.wav'):
                feat = extract_features_scaled(os.path.join(folder_path, fname), scaler)
                if feat is not None:
                    X.append(feat)
                    y.append(idx)
    
    X = np.array(X).reshape(-1, MAX_LEN, N_MFCC, 1)
    y = np.array(y)
    
    # 3. Split 70/15/15
    X_train, X_temp, y_train, y_temp = train_test_split(X, y, test_size=0.3, stratify=y, random_state=42)
    X_val, X_test, y_val, y_test = train_test_split(X_temp, y_temp, test_size=0.5, stratify=y_temp, random_state=42)
    
    # 4. Augmentare
    X_train, y_train = augment_data(X_train, y_train)

    # 5. Callbacks
    callbacks = [
        tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True),
        tf.keras.callbacks.ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3)
    ]

    # 6. Build & Train
    model = build_cnn_model(input_shape=(MAX_LEN, N_MFCC, 1), num_classes=len(classes))
    
    history = model.fit(
        X_train, y_train, 
        epochs=EPOCHS, 
        batch_size=BATCH_SIZE, 
        validation_data=(X_val, y_val), 
        callbacks=callbacks, 
        verbose=1
    )

    # 7. Salvare Istoric CSV (CERINTA NOUA)
    save_training_history(history)

    # 8. Evaluare si Salvare Model
    print("\n--- Evaluare Finala ---")
    loss, acc = model.evaluate(X_test, y_test)
    print(f"Test Accuracy: {acc*100:.2f}%")
    
    y_pred_probs = model.predict(X_test)
    y_pred = np.argmax(y_pred_probs, axis=1)
    
    print(classification_report(y_test, y_pred, target_names=classes))
    
    if acc >= 0.65:
        model.save(os.path.join(MODELS_DIR, "trained_model.h5"))
        print("✅ Model salvat.")
    else:
        print("⚠️ Modelul nu a atins targetul de 65%.")

    plot_training_results(history, y_test, y_pred, classes)

if __name__ == "__main__":
    main()