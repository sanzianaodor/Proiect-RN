# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale
**Instituție:** POLITEHNICA București – FIIR
**Student:** Odor Sînziana-Gabriela
**Link Repository GitHub:** https://github.com/sanzianaodor/Proiect-RN.git
**Data:** 27.11.2025

---

## Introducere

Acest document descrie activitățile realizate în **Etapa 3**, în care se analizează și se preprocesează setul de date necesar proiectului „Rețele Neuronale". Scopul etapei este pregătirea corectă a datelor pentru instruirea modelului RN, respectând bunele practici privind calitatea, consistența și reproductibilitatea datelor.

---

##  1. Structura Repository-ului Github (versiunea Etapei 3)

```
project-name/
├── README.md
├── docs/
│   └── datasets/          # descriere seturi de date, surse, diagrame
├── data/
│   ├── raw/               # date brute
│   ├── processed/         # date curățate și transformate
│   ├── train/             # set de instruire
│   ├── validation/        # set de validare
│   └── test/              # set de testare
├── src/
│   ├── preprocessing/     # funcții pentru preprocesare
│   ├── data_acquisition/  # generare / achiziție date (dacă există)
│   └── neural_network/    # implementarea RN (în etapa următoare)
├── config/                # fișiere de configurare
└── requirements.txt       # dependențe Python (dacă aplicabil)
```

---

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Set de date hibrid, compus din surse externe și achiziție proprie, totalizând 320 de eșantioane audio:
    * **Vioară și Tobe:** Preluate din dataset-ul public Kaggle *"Music Instrument Sounds For Classification"* (autor: Abdulvahap).
    * **Chitară și Pian:** Dataset constituit din:
        * 50% (40 fișiere/instrument) – înregistrări fizice proprii ale instrumentelor reale.
        * 50% (40 fișiere/instrument) – generate software utilizând biblioteca de instrumente virtuale GarageBand.
* **Modul de achiziție:** Senzori reali (microfon), Simulare (GarageBand), Fișier extern (Kaggle) 
* **Perioada / condițiile colectării:** Noiembrie 2025 - Ianuarie 2026.

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 320 
* **Număr de caracteristici (features):** 4
* **Tipuri de date:** Audio.
* **Format fișiere:** `.wav` .

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Descriere** | **Domeniu valori** |
|-------------------|---------|---------------|--------------------|
| **Chitară** | Proprie | Înregistrări acustice | 40 |
| **Pian** | Proprie | Înregistrări pian | 40 |
| **Tobe** | Extern | Percuție / Loop-uri ritmice | 40 |
| **Vioară** | Extern | Instrumente cu coarde (arcuș) | 40 |

**Fișier recomandat:**  `data/README.md`

---

##  3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate

### 3.1 Statistici descriptive aplicate

* **Durata semnalelor (Medie, Min-Max):** Variație mare între dataset-ul Kaggle (clipuri scurte) și înregistrările proprii.
* **Amplitudine și Volum (Deviație standard):** Fișierele din GarageBand au amplitudine maximă constantă, în timp ce înregistrările reale au variații mari de volum.
* **Rata de eșantionare (Sample Rate):** S-au identificat mix-uri de 44.1 kHz și 48 kHz, necesitând resampling uniform.
* **Distribuția claselor:** Verificarea echilibrului dataset-ului (Histogramă: distribuție perfect uniformă, 25% per clasă).

### 3.2 Analiza calității datelor

* **Detectarea valorilor lipsă sau corupte:**
    * S-a verificat integritatea celor 320 de fișiere audio. Nu s-au identificat fișiere corupte (unreadable).
    * S-au identificat segmente de "lipsă informație" (liniște completă) la începutul și finalul înregistrărilor proprii, care necesită eliminare.
* **Detectarea valorilor inconsistente sau eronate:**
    * **Rate de eșantionare mixte:** Fișierele provin cu rate diferite, necesitând resampling obligatoriu.
    * **Canale audio:** Mix de fișiere Mono (Kaggle) și Stereo (GarageBand). Conversia la Mono este necesară pentru consistența input-ului în rețea.
  

### 3.3 Probleme identificate

* **Bias de sursă (Source Bias):** S-a identificat o corelație nedorită între *prezența zgomotului de fond* și clasele Chitară/Pian (provenite parțial din microfon), comparativ cu puritatea semnalului la Tobe/Vioară (Kaggle). 

* **Neuniformitate temporală:** Variația duratei fișierelor (de la 3s la 7s) împiedică formarea unor tensori de intrare cu dimensiuni fixe, necesitând o strategie strictă de trunchiere (trimming).

---

##  4. Preprocesarea Datelor

### 4.1 Curățarea datelor

### 4.1 Curățarea datelor

* **Eliminare duplicate și verificare integritate:**
    * Verificarea consistenței fișierelor audio; eliminarea oricărui fișier care nu poate fi decodat de librăria `librosa`.
    * Asigurarea unicității numelor de fișiere în structura de foldere.
* **Tratarea inconsecvențelor temporale (Durată variabilă):**
    * **Silence Trimming:** Eliminarea automată a zonelor de liniște (sub -60dB) de la începutul și finalul înregistrărilor proprii (microfon) pentru a centra informația utilă.
    * **Uniformizare lungime:** Aducerea tuturor eșantioanelor la o dimensiune fixă de **3 secunde** (sau numărul echivalent de cadre):
        * *Cazul Lung:* Trunchiere (se păstrează primele 3 secunde după trim).
        * *Cazul Scurt:* Zero-padding (completare cu 0 la final până la atingerea lungimii).

### 4.2 Transformarea caracteristicilor

* **Normalizare:** Min–Max / Standardizare
* **Encoding pentru variabile categoriale**

### 4.3 Structurarea seturilor de date

**Împărțire recomandată:**
* 70–80% – train
* 10–15% – validation
* 10–15% – test

**Principii respectate:**
* Stratificare pentru clasificare
* Fără scurgere de informație (data leakage)
* Statistici calculate DOAR pe train și aplicate pe celelalte seturi

### 4.4 Salvarea rezultatelor preprocesării

* Date preprocesate în `data/processed/`
* Seturi train/val/test în foldere dedicate
* Parametrii de preprocesare în `config/preprocessing_config.*` (opțional)

---

##  5. Fișiere Generate în Această Etapă

* `data/raw/` – date brute
* `data/processed/` – date curățate & transformate
* `data/train/`, `data/validation/`, `data/test/` – seturi finale
* `src/preprocessing/` – codul de preprocesare
* `data/README.md` – descrierea dataset-ului

---

##  6. Stare Etapă (de completat de student)

- [X] Structură repository configurată
- [X] Dataset analizat (EDA realizată)
- [X] Date preprocesate
- [X] Seturi train/val/test generate
- [X] Documentație actualizată în README + `data/README.md`

---
