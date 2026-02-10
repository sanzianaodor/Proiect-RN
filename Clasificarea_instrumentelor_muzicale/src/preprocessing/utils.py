import librosa
import numpy as np
import soundfile as sf
import config
import os

def load_and_fix_length(file_path):
    """Incarca, face Mono si taie/completeaza la 3 secunde."""
    try:
        # Incarcare
        signal, sr = librosa.load(file_path, sr=config.SAMPLE_RATE, mono=True)
        
        # Trim Silence
        signal, _ = librosa.effects.trim(signal, top_db=20)
        
        # Fixare lungime
        length = len(signal)
        if length > config.SAMPLES_PER_TRACK:
            signal = signal[:config.SAMPLES_PER_TRACK]
        else:
            padding = config.SAMPLES_PER_TRACK - length
            signal = np.pad(signal, (0, padding), mode='constant')
            
        return signal
    except Exception as e:
        print(f"Eroare fisier {file_path}: {e}")
        return None

def save_audio(signal, folder, filename):
    """Salveaza semnalul ca fisier .WAV"""
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    sf.write(path, signal, config.SAMPLE_RATE)

def add_noise(signal, noise_factor=0.005):
    """Adauga zgomot"""
    noise = np.random.randn(len(signal))
    return signal + noise_factor * noise

def change_pitch(signal, steps=2):
    """Schimba tonalitatea"""
    return librosa.effects.pitch_shift(y=signal, sr=config.SAMPLE_RATE, n_steps=steps)