import tensorflow as tf
from tensorflow.keras import layers, models, optimizers
import os

def create_audio_cnn(input_shape, num_classes):
    """
    Definește și compilează arhitectura Rețelei Neuronale Convoluționale (CNN)
    pentru clasificarea instrumentelor muzicale.

    Această arhitectură este proiectată pentru a procesa Spectrograme Mel (imagini 2D)
    și a identifica timbrul specific al instrumentului.

    Parameters:
    -----------
    input_shape : tuple
        Dimensiunea input-ului (înălțime, lățime, canale). 
        Exemplu: (128, 94, 1) -> 128 benzi Mel, 94 frame-uri de timp, 1 canal (mono).
    num_classes : int
        Numărul de clase de ieșire (ex: 4 pentru Pian, Vioară, Chitară, Tobe).

    Returns:
    --------
    model : tf.keras.Model
        Modelul compilat, gata de antrenare.

    Arhitectura Detaliată:
    ----------------------
    1. Input Layer:
       - Primește matricea spectrogramă.
    
    2. Blocuri Convoluționale (Feature Extraction):
       - Conv2D (32 filtre): Detectează trăsături simple (linii, margini în spectru).
       - MaxPooling2D: Reduce dimensiunea spațială, păstrând trăsăturile dominante 
         și reducând costul computațional.
       - Conv2D (64 filtre): Detectează tipare mai complexe (armonice, atacul sunetului).
       - MaxPooling2D: Continuă reducerea dimensionalității.
       - Conv2D (128 filtre): Extrage trăsături de nivel înalt specifice timbrului.
    
    3. Flatten Layer:
       - Transformă matricea 3D într-un vector 1D pentru straturile dense.

    4. Dense Layers (Classification Head):
       - Dense (128 neuroni): Procesează combinațiile de trăsături extrase.
       - Dropout (0.5): Previne overfitting-ul prin dezactivarea aleatorie a 50% din neuroni.
       - Output Layer (Softmax): Calculează probabilitatea pentru fiecare clasă (suma = 1.0).
    """
    
    model = models.Sequential([
        # --- Bloc 1: Extragere Trăsături de Nivel Jos ---
        layers.Input(shape=input_shape),
        
        layers.Conv2D(32, (3, 3), activation='relu', padding='same', name='conv_1'),
        layers.MaxPooling2D((2, 2), name='pool_1'),
        layers.BatchNormalization(name='norm_1'), # Normalizează activările pentru stabilitate

        # --- Bloc 2: Extragere Trăsături de Nivel Mediu ---
        layers.Conv2D(64, (3, 3), activation='relu', padding='same', name='conv_2'),
        layers.MaxPooling2D((2, 2), name='pool_2'),
        layers.BatchNormalization(name='norm_2'),

        # --- Bloc 3: Extragere Trăsături de Nivel Înalt ---
        layers.Conv2D(128, (3, 3), activation='relu', padding='same', name='conv_3'),
        layers.MaxPooling2D((2, 2), name='pool_3'),
        
        # --- Clasificator (Fully Connected) ---
        layers.Flatten(name='flatten'),
        
        layers.Dense(128, activation='relu', name='dense_hidden'),
        layers.Dropout(0.5, name='dropout'), # Regularizare esențială pentru seturi mici de date
        
        # Stratul Final: num_classes neuroni cu activare Softmax
        layers.Dense(num_classes, activation='softmax', name='output_layer')
    ])

    # Compilarea Modelului
    # Optimizer: Adam (standard industrial, convergență rapidă)
    # Loss: Categorical Crossentropy (pentru clasificare multi-clasă One-Hot encoded)
    # Metrics: Accuracy
    model.compile(
        optimizer='adam',
        loss='categorical_crossentropy',
        metrics=['accuracy']
    )

    return model

def main():
    # --- Configurație Demo pentru Etapa 4 ---
    # Presupunem spectrograme de 128 benzi Mel și aprox 3 secunde (~94 frames)
    # Canale = 1 (Alb-Negru/Mono)
    INPUT_SHAPE = (128, 94, 1) 
    NUM_CLASSES = 4
    
    print("--- Modul 2: Definire Arhitectură RN ---")
    
    # 1. Instanțiere Model
    model = create_audio_cnn(INPUT_SHAPE, NUM_CLASSES)
    
    # 2. Afișare Sumar (Demonstrează structura)
    model.summary()
    
    # 3. Salvare Model Neantrenat (Schelet)
    # Calea relativă către folderul models
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    models_dir = os.path.join(base_dir, 'models')
    
    if not os.path.exists(models_dir):
        os.makedirs(models_dir)
        
    save_path = os.path.join(models_dir, 'instrument_classifier_skeleton.h5')
    model.save(save_path)
    
    print(f"\n[SUCCES] Arhitectura a fost definită, compilată și salvată în:")
    print(f"{save_path}")
    print("Notă: Acesta este un model neantrenat (greutăți aleatorii), gata pentru Etapa 5.")

if __name__ == "__main__":
    main()