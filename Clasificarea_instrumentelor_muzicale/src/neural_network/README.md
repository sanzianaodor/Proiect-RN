# Modulul Rețea Neuronală (Arhitectura CNN)

Acest fisier conține codul sursă pentru definirea modelului de Inteligență Artificială. Aici este construit "creierul" care ia decizia finală (Chitară vs Pian vs Tobe vs Vioară).

## 1. De ce am ales CNN (Rețele Convoluționale)?

Deși sunetul este invizibil (o serie de vibrații în timp), noi îl transformăm într-o **imagine** numită *spectrogramă* (o "hartă" a frecvențelor).

Deoarece datele noastre arată acum ca niște imagini, am ales **CNN (Convolutional Neural Network)**, arhitectura standard în industrie pentru recunoașterea vizuală.
* **Analogie:** Rețeaua se uită la sunet exact cum un om se uită la o radiografie, căutând tipare vizuale specifice (linii orizontale pentru corzi, linii verticale pentru tobe).

## 2. Diagrama Logică a Modelului

Modelul este construit pe etaje (Layers), fiecare având un rol specific în procesarea informației:

   INTRARE (Input)
      │
      ▼
[ ETAPA 1: Extragere Trăsături Simple ]
   │  • Detectează muchii și schimbări bruște de sunet.
   │  • Micșorează imaginea (păstrează doar esențialul).
   │
[ ETAPA 2: Extragere Timbru ]
   │  • Detectează tipare complexe (ex: vibrația specifică a corzii).
   │  • "Uită" intenționat informație pentru a nu "toci" datele (evită Overfitting).
   │
[ ETAPA 3: Rafinare ]
   │  • Scanează imaginea la un nivel și mai detaliat.
   │
[ ETAPA 4: Clasificare (Decision Making) ]
   │  • Transformă matricea 2D într-o listă lungă de numere.
   │  • Calculează probabilitățile finale.
      │
      ▼
   IEȘIRE: [ % Chitară, % Pian, % Tobe, % Vioară ]

## 3. Descrierea Modulelor Implementate

Proiectul este împărțit în trei module software distincte, conform cerințelor de curs:

### 3.1. Modulul de Achiziție și Logare (`src/data_acquisition/`)
* **Scop:** Gestionarea setului de date și asigurarea trasabilității.
* **Funcționalitate:** Scriptul `generate.py` scanează folderul `data/raw`, extrage metadate tehnice (durată, sample rate) și generează un raport CSV (`docs/acquisition_log.csv`).
* **Contribuție Proprie:** Identifică automat fișierele înregistrate personal (microfon) față de cele sintetice sau externe, validând cerința de **min. 40% date originale**.

### 3.2. Modulul Rețea Neuronală (`src/neural_network/`)
* **Tehnologie:** TensorFlow / Keras.
* **Arhitectură:** **CNN (Convolutional Neural Network)** cu 3 blocuri de convoluție + MaxPooling și straturi Dense finale.
* **Status:** Arhitectura este complet definită și compilată. Modelul este salvat în format `.h5` (`models/untrained_model.h5`) cu ponderi inițializate aleator, pregătit pentru etapa viitoare de antrenare.

### 3.3. Modulul Interfață și Inferență (`src/app/` + LabVIEW)
* **Backend (Python):** Scriptul `main.py` acționează ca un server de procesare.
    * Primește calea fișierului ca argument CLI.
    * Rezolvă compatibilitatea caracterelor pentru a comunica cu Windows.
    * Returnează decizia finală în `stdout`.
* **Frontend (LabVIEW):** VI-ul principal apelează scriptul Python prin funcția `System Exec`.
    * Afișează vizual instrumentul detectat și gradul de încredere (Confidence %).

---