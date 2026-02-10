import os
import tensorflow as tf
# Folosim importul standard. Chiar daca apare cu galben in VS Code, ESTE CORECT.
from tensorflow.keras import layers, models # type: ignore
import sys

# Incercam sa importam config-ul pentru a lua numarul de clase automat
try:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'preprocessing')))
    import config
    NUM_CLASSES = len(config.CLASSES) 
    INPUT_SHAPE = (130, 13, 1) 
except ImportError:
    NUM_CLASSES = 4
    INPUT_SHAPE = (130, 13, 1)

def build_cnn_model(input_shape=INPUT_SHAPE, num_classes=NUM_CLASSES):
    """
    Defineste arhitectura Retelei Neuronale Convolitionale (CNN).
    """
    model = models.Sequential([
        # --- Blocul 1 ---
        layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape, padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.BatchNormalization(), # Acum va functiona corect

        # --- Blocul 2 ---
        layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.3),

        # --- Blocul 3 ---
        layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
        layers.MaxPooling2D((2, 2)),
        layers.Dropout(0.3),

        # --- Blocul 4 ---
        layers.Flatten(),
        layers.Dense(64, activation='relu'),
        layers.Dense(num_classes, activation='softmax')
    ])

    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])
    
    return model

def save_model_skeleton(model, filename="untrained_model.h5"):
    """Salveaza modelul pe disc."""
    # Salvam direct in folderul models din root
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    save_path = os.path.join(base_dir, "models", filename)
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    model.save(save_path)
    print(f"✅ Model salvat cu succes in: {save_path}")

def load_model_skeleton(filename="untrained_model.h5"):
    """Incarca modelul de pe disc."""
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    path = os.path.join(base_dir, "models", filename)
    
    if os.path.exists(path):
        model = tf.keras.models.load_model(path)
        print(f"✅ Model incarcat din: {path}")
        return model
    else:
        print(f"❌ Fisierul nu exista: {path}")
        return None

if __name__ == "__main__":
    print("--- Modul 2: Neural Network Initialization ---")
    
    # 1. Construim modelul
    model = build_cnn_model()
    
    # 2. Afisam rezumatul
    model.summary()
    
    # 3. Testam salvarea (cu numele corect untrained_model.h5)
    save_model_skeleton(model)
    
    # 4. Testam reincarcarea
    loaded_model = load_model_skeleton()
    
    print("\nREZULTAT: Modulul RN este functional, arhitectura este definita si compilata.")