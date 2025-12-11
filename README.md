# 📘 README – Etapa 3: Analiza și Pregătirea Setului de Date pentru Rețele Neuronale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Odor Sînziana-Gabriela
**Data:** 20.11.2025

---

## Introducere

Acest document descrie activitățile realizate în **Etapa 3**, în care se analizează și se preprocesează setul de date necesar proiectului „Rețele Neuronale". Scopul etapei este pregătirea corectă a datelor pentru instruirea modelului RN, respectând bunele practici privind calitatea, consistența și reproductibilitatea datelor.

---

##  1. Structura Repository-ului Github (versiunea Etapei 3)

```
Clasificarea-instrumentelor-muzicale/
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

## 2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** Dataset public 
* **Modul de achiziție:** Descărcare fișier extern, apoi organizare manuală pe clase.
* **Perioada / condițiile colectării:** Noiembrie 2024 - Ianuarie 2025.

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații (fișiere):** **80** (20 per clasă)
* **Număr de caracteristici (Clase):** 4
* **Tipuri de date:** Sunete (serii temporale)
* **Format fișiere:** WAV (majoritar)

### 2.3 Descrierea fiecărei caracteristici (Clase de instrumente)

| **Clasă** | **Tip** | **Unitate** | **Descriere** | **Număr Observații** |
| :--- | :--- | :--- | :--- | :--- |
| **chitară** | sound | - | Clasa de ieșire  | 20 |
| **pian** | sound | – | Clasa de ieșire | 20 |
| **tobe** | sound | - | Clasa de ieșire | 20 |
| **vioară** | sound | - | Clasa de ieșire | 20 |

---

## 3. Analiza Exploratorie a Datelor (EDA) – Sintetic

### 3.1 Statistici descriptive aplicate (Pe datele brute)

* **Medie, deviație standard:** Aplicată pe **durata fișierelor** și **amplitudinea RMS** pentru a înțelege varianța sunetelor.
* **Distribuții pe caracteristici:** Histograme ale duratei și ale frecvenței de eșantionare inițiale.

### 3.2 Analiza calității datelor

* **Detectarea valorilor inconsistente:** Identificarea fișierelor cu **frecvență de eșantionare non-standard** sau **mono/stereo inconsistent**.
* **Identificarea redundanțelor:** Eliminarea fișierelor audio duplicate.

### 3.3 Probleme identificate

* **Variabilitate a Frecvenței de Eșantionare (SR):** Fișierele au SR-uri diferite (ex: 44.1 kHz vs 22.05 kHz) - **Necesită reeșantionare**.
* **Variabilitate a Duratei:** Lungimea fișierelor variază - **Necesită uniformizare (trunchiere/padding)**.

---

## 4. Preprocesarea Datelor

### 4.1 Curățarea și Uniformizarea Datelor

* **Uniformizare Frecvență:** Toate fișierele sunt **reesantionate** la **$16 \text{ kHz}$** (frecvență optimă pentru AI audio).
* **Uniformizare Lungime:** Toate fișierele sunt ajustate la o durată fixă de **$3.0$ secunde** prin **trunchiere** sau **padding cu zerouri**.
* **Salvare:** Rezultatele uniformizării sunt salvate în `data/processed/` sub forma de fișiere WAV.

### 4.2 Transformarea Caracteristicilor (Feature Extraction)

* **Extracția Caracteristicilor:** Din fișierele WAV uniformizate, se extrag **Spectrograme Mel-Scală**. Aceasta este forma de date de intrare finală pentru Rețeaua Neuronală Convoluțională (CNN).
* **Normalizare:** Spectrogramele sunt normalizate (ex: **Standardizare Z-Score**) pentru a asigura stabilitatea antrenării RN.

### 4.3 Structurarea Seturilor de Date

* **Împărțire:** Train: $75\%$; Validation: $15\%$; Test: $10\%$.
* **Principii respectate:**
    * **Stratificare:** Se asigură un număr aproximativ egal de observații per clasă (instrument) în fiecare set.
    * **Fără *data leakage***: Parametrii de normalizare sunt calculați **DOAR** pe setul de *train* și apoi aplicați pe seturile de *validation* și *test*.

### 4.4 Salvarea rezultatelor preprocesării

* Datele uniformizate (WAV) sunt în `data/processed/`.
* Seturile finale (Spectrogramele Normalizate) sunt salvate în folderele `data/train/`, `data/validation/`, și `data/test/`.

---

## 5. Fișiere Generate în Această Etapă

* `data/raw/` – date brute
* `data/processed/` – date curățate & uniformizate
* `data/{train/val/test}/` – Matricele finale (Spectrograme) pentru instruire
* `src/preprocessing/preprocess_data.py` – Codul Python pentru uniformizare și feature extraction
* `config/preprocessing_config.json` – Fișier ce stochează TARGET_SR, TARGET_DURATION și parametrii de normalizare.

---

## 6. Stare Etapă 

- [x] Structură repository configurată
- [x] Dataset analizat (EDA realizată - durată, SR)
- [x] Date preprocesate (Uniformizare $16 \text{ kHz}$, $3.0 \text{ s}$)
- [ ] Seturi train/val/test generate (Spectrograme extrase și salvate)
- [x] Documentație actualizată în README + `data/README.md`



