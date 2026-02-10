import streamlit as st
import os
import numpy as np
import librosa
import tensorflow as tf
import pickle
import time

# --- 1. CONFIGURARE PAGINĂ ---
st.set_page_config(
    page_title="AI Music Classifier",
    page_icon="🎵",
    layout="centered"
)

# --- 2. CĂI ȘI PARAMETRI (Relative) ---
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
MODEL_PATH = os.path.join(BASE_DIR, "models", "optimized_model.h5")
SCALER_PATH = os.path.join(BASE_DIR, "config", "preprocessing_params.pkl")

# Parametri Audio
SAMPLE_RATE = 22050
DURATION = 3 
N_MFCC = 13
MAX_LEN = 130 
CLASS_NAMES = ['Chitara', 'Pian', 'Tobe', 'Vioara']

# --- 3. FUNCȚII DE ÎNCĂRCARE (Cu Caching pentru viteză) ---
@st.cache_resource
def load_resources():
    """Încarcă modelul și scaler-ul o singură dată la pornire"""
    try:
        model = tf.keras.models.load_model(MODEL_PATH)
        with open(SCALER_PATH, 'rb') as f:
            scaler = pickle.load(f)
        return model, scaler
    except Exception as e:
        return None, None

def process_audio(file_path, scaler):
    """Transformă audio în input pentru CNN"""
    try:
        # Încărcare cu Librosa
        y, sr = librosa.load(file_path, sr=SAMPLE_RATE, duration=DURATION)
        
        # Padding/Trimming
        expected_samples = int(SAMPLE_RATE * DURATION)
        if len(y) < expected_samples:
            y = np.pad(y, (0, expected_samples - len(y)))
        else:
            y = y[:expected_samples]
            
        # MFCC
        mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=N_MFCC)
        
        # Ajustare dimensiune
        if mfcc.shape[1] > MAX_LEN:
            mfcc = mfcc[:, :MAX_LEN]
        else:
            mfcc = np.pad(mfcc, ((0, 0), (0, MAX_LEN - mfcc.shape[1])))
            
        # Scalare (folosind scaler-ul antrenat)
        mfcc_scaled = scaler.transform(mfcc.T)
        
        # Reshape pentru CNN (Batch, Time, Freq, Channels)
        return mfcc_scaled.reshape(1, MAX_LEN, N_MFCC, 1)
    except Exception as e:
        st.error(f"Eroare preprocesare: {e}")
        return None

# --- 4. INTERFAȚA GRAFICĂ (UI) ---
st.title("🎵 Clasificare Instrumente Muzicale")
st.markdown("Această aplicație folosește o **Rețea Neuronală Convoluțională (CNN)** pentru a identifica instrumentul din fișiere audio.")

# Încărcare resurse în fundal
model, scaler = load_resources()

if model is None or scaler is None:
    st.error(" EROARE CRITICĂ: Nu s-a putut încărca modelul sau scalerul! Verifică folderul 'models' și 'config'.")
    st.stop()
else:
    st.success("Sistem AI Online: Model încărcat și pregătit.", icon="🟢")

st.divider()

# Zona de Upload
uploaded_file = st.file_uploader("Încarcă un fișier .WAV", type=["wav"])

if uploaded_file is not None:
    # Salvăm fișierul temporar pentru procesare
    with open("temp_audio.wav", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    # Player Audio
    st.subheader("= Previzualizare Audio")
    st.audio(uploaded_file, format='audio/wav')
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        analyze_btn = st.button("Analizează Instrumentul", use_container_width=True, type="primary")

    if analyze_btn:
        with st.spinner('Se extrag caracteristici MFCC și se rulează inferența...'):
            # Simulare procesare (pentru efect vizual)
            time.sleep(0.5) 
            
            # Procesare reală
            input_data = process_audio("temp_audio.wav", scaler)
            
            if input_data is not None:
                # Predicție
                prediction = model.predict(input_data)
                scores = prediction[0]
                idx = np.argmax(scores)
                label = CLASS_NAMES[idx]
                confidence = scores[idx] * 100
                
                # Afișare Rezultate
                st.divider()
                
                # Layout pe coloane pentru rezultat
                r_col1, r_col2 = st.columns(2)
                
                with r_col1:
                    st.subheader("Instrument Detectat")
                    st.markdown(f"<h1 style='text-align: center; color: #4CAF50;'>{label}</h1>", unsafe_allow_html=True)
                
                with r_col2:
                    st.subheader("Nivel de Încredere")
                    st.markdown(f"<h1 style='text-align: center;'>{confidence:.2f}%</h1>", unsafe_allow_html=True)

                # Validare Threshold
                if confidence < 60.0:
                    st.warning(" Atenție: Scorul este sub 60%. Rezultatul poate fi incert (Zgomot?).")
                elif confidence > 90.0:
                    st.balloons()

                # Grafic Detaliat
                st.subheader(" Analiză Probabilități per Clasă")
                st.bar_chart(dict(zip(CLASS_NAMES, scores)))