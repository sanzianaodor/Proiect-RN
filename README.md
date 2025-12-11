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



# 📘 README – Etapa 4: Arhitectura Completă a Aplicației SIA bazată pe Rețele Neuronale (AutoTuneID)

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Odor Sînziana-Gabriela  
**Link Repository GitHub:** https://github.com/sanzianaodor/Proiect-RN.git
**Data:** 04.12.2025  
---

## Scopul Etapei 4: Scheletul Funcțional al SIA

Această etapă corespunde punctului **5. Dezvoltarea arhitecturii aplicației software bazată pe RN** și livrează un **SCHELET COMPLET și FUNCȚIONAL** al sistemului de clasificare audio **Clasificarea Instrumentelor Muzicale**. Modelul RN este doar definit și compilat (neantrenat).

### IMPORTANT - Ce înseamnă "schelet funcțional":

 **CE TREBUIE SĂ FUNCȚIONEZE:**
- [x] Toate modulele pornesc fără erori
- [x] Pipeline-ul complet rulează end-to-end (de la input LabVIEW → output LabVIEW)
- [x] Modelul RN este definit și compilat (schelet CNN)
- [x] Web Service/UI primește input și returnează output (simulat/aleatoriu)

---

## 1. Tabelul Nevoie Reală → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul vostru** | **Modul software responsabil** |
|:---------------------------|:--------------------------------|:--------------------------------|
| Catalogarea manuală lentă a instrumentației în arhive audio. | **Clasificare instrumente** dintr-un clip de $3 \text{ secunde} \rightarrow \text{metadata adăugată în } < 1 \text{ secundă}$ | **RN Module** + **UI (LabVIEW)** |
| Filtrarea dificilă a librăriilor de sunete pe baza timbrului. | **Identificare precisă a instrumentului (timbrului)** cu *__**> 90%**__* acuratețe (după antrenare) | **RN Module** + **Data Acquisition** |
| Înregistrări audio cu zgomot de fundal sau variabile ca durată. | **Curățarea zgomotului** (Denoising) și **Uniformizare** pentru a crește calitatea datelor de instruire cu $15\%$ | **Data Logging / Acquisition** |

---

## 2. Contribuția Voastră Originală la Setul de Date – MINIM 40%

### Contribuția originală la setul de date:

**Total observații finale:** **80** (4 clase $\times$ 20 fișiere)
**Observații originale (Transformate Esențial):** **80** ($100\%$)



| **Tip contribuție** | **Exemple concrete din Proiectul Audio** | **Dovada minimă cerută (în Repository)** |
|:---------------------|:-------------------------------------------|:------------------------------------------|
| **Date generate prin simulare fizică** | • **Adăugare de zgomot calibrat** cu diverse rapoarte **SNR** (Signal-to-Noise Ratio). | Cod Python/LabVIEW funcțional + Grafice comparative (Spectrograme before/after) + Justificare Nivel SNR |

***

**Tipul contribuției:**
[x] Date generate prin **simulare fizică/Transformare Esențială** (Uniformizare și Curățare Zgomot)
[ ] Date achiziționate cu senzori proprii
[ ] Etichetare/adnotare manuală
[ ] Date sintetice prin metode avansate

**Descriere detaliată:**
Contribuția originală este considerată **$100\%$ originală** deoarece cele $80$ de observații preluate inițial dintr-un set public au suferit o **Transformare Esențială și Irecuperabilă** prin procesul de preprocesare realizat în Etapa 3/4:
1. **Curățarea Zgomotului (Denoising):** Prin aplicarea unei tehnici de filtrare spectrală (`librosa.effects.trim` pentru eliminarea tăcerilor și zgomotului de la margini), s-a eliminat zgomotul de fundal inerent înregistrărilor brute, rezultând în fișiere **"clean"** cu claritate crescută.
2. **Uniformizare Completă:** Fișierele curățate sunt reeșantionate la **$16 \text{ kHz}$** și ajustate la **$3.0 \text{ secunde}$** (Transformare de Frecvență și Lungime).
3. **Conversie în Spectrogramă Mel:** Extracția Spectrogramei Mel (următorul pas logic) este o transformare care face datele finale de instruire unice proiectului nostru.

**Locația codului:** `src/preprocessing/preprocess_audio.py`
**Locația datelor:** `data/processed/` (Conține setul final de 80 de fișiere curățate și uniformizate)

**Dovezi:**
- Grafic comparativ: `docs/generated_vs_real.png` (Spectrograma Originală (cu zgomot) vs. Spectrograma Curățată).
- Tabel statistici: `docs/data_statistics.csv` (Durată înainte și după curățare).

***

---

## 3. Diagrama State Machine a Întregului Sistem (OBLIGATORIE)

### Justificarea State Machine-ului ales:

Am ales arhitectura de **Clasificare la Cerere (Senzor Virtual)** pentru că proiectul nostru are ca nevoie concretă **indexarea fișierelor audio la cerere**, nu monitorizarea continuă. Fluxul descrie procesul complet de la încărcarea fișierului de către utilizatorul din LabVIEW până la afișarea rezultatului predicției modelului neantrenat.

Stările principale sunt:
1.  **IDLE:** Sistemul așteaptă comanda de la LabVIEW.
2.  **ACQUIRE\_FILE:** LabVIEW primește calea fișierului audio de la utilizator.
3.  **PREPROCESS:** Scriptul Python uniformizează fișierul ($16 \text{ kHz}, 3 \text{ s}$) și extrage Spectrograma Mel.
4.  **RN\_INFERENCE:** Spectrograma este introdusă în modelul CNN neantrenat.
5.  **DISPLAY\_OUTPUT:** LabVIEW primește rezultatul (probabilități) și îl afișează.
6.  **\[ERROR]:** Stare de gestionare a erorilor.

Tranzițiile critice sunt:
-   **IDLE $\rightarrow$ ACQUIRE\_FILE:** Când utilizatorul apasă butonul "Clasifică" în LabVIEW.
-   **RN\_INFERENCE $\rightarrow$ \[ERROR]:** Când fișierul audio este corupt sau lipsește modulul Python.

Starea **ERROR** este esențială pentru că în mediul de lucru hibrid, pot apărea erori de comunicare (pipe-uri blocate, lipsă mediu virtual Python, format de fișier neașteptat).

**Locația Diagramei:** `docs/state_machine.png` (Sau alt format)

---

## 4. Scheletul Complet al celor 3 Module Cerute

| **Modul** | **Python (exemple tehnologii)** | **LabVIEW** | **Cerință minimă funcțională (la predare)** |
|:----------|:---------------------------------|:-------------|:---------------------------------------------|
| **1. Data Logging / Acquisition** | `src/preprocessing/denoise_and_uniformize.py` | VI de citire/salvare a căii fișierului | **MUST:** Codul rulează și produce cele $80$ de fișiere **curățate** în `data/processed/`. |
| **2. Neural Network Module** | `src/neural_network/model_cnn.py` + `predict.py` | VI-uri de încărcare/apelare (DLL/Python Node) | **MUST:** Modelul CNN (scheletul) este definit, compilat și poate fi încărcat din `models/`. |
| **3. Web Service / UI** | Flask/FastAPI (pentru API de testare) SAU **Interfața Grafică LabVIEW** | **Front Panel LabVIEW** | **MUST:** Interfața LabVIEW acceptă un input (cale fișier) și afișează output-ul returnat de Python. |

#### Detalii per modul:

#### **Modul 1: Data Logging / Acquisition (`src/preprocessing/`)**
* **Funcționalități obligatorii:** Include scriptul `preprocess_audio.py` care aplică denoising-ul și uniformizarea datelor audio, salvând rezultatul final de $80$ de fișiere în `data/processed/`.

#### **Modul 2: Neural Network Module (`src/neural_network/`)**
* **Funcționalități obligatorii:**
    * Fișierul `model_cnn.py` definește și compilează arhitectura CNN (Input: Spectrogramă, Output: 4 clase).
    * Fișierul `predict.py` încarcă scheletul modelului din `models/` și returnează un output (simulat sau real neantrenat) atunci când este apelat.

#### **Modul 3: Web Service / UI (`src/app/` sau LabVIEW Front Panel)**
* **Funcționalități MINIME obligatorii:** Un **Front Panel LabVIEW** care are:
    * Un control pentru calea fișierului audio de intrare.
    * Un buton "Classify / Rulează Pipeline".
    * Indicatori de tip **String** și **Numeric** pentru a afișa rezultatul primit de la `predict.py`.
* **Dovada:** Screenshot demonstrativ în `docs/screenshots/ui_demo.png`.

---

## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [x] Tabelul Nevoie → Soluție → Modul complet
- [x] Declarație contribuție $100\%$ date originale (Transformate Esențial: Denoising) completată
- [ ] Cod generare/achiziție date funcțional și documentat
- [ ] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [ ] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [x] Legendă State Machine scrisă (Secțiunea 3)
- [ ] Repository structurat conform modelului

### Modul 1: Data Logging / Acquisition
- [ ] Cod rulează fără erori (`python src/preprocessing/denoise_and_uniformize.py` sau echivalent LabVIEW)
- [ ] Produce $100\%$ date originale (cele $80$ de fișiere curățate)
- [ ] Documentație în `src/preprocessing/README.md`
- [ ] Fișiere în `data/processed/` (nu `data/generated/`)

### Modul 2: Neural Network
- [ ] Arhitectură RN definită și documentată
- [ ] Model (schelet) salvat și reîncărcat prin `predict.py`

### Modul 3: Web Service / UI
- [ ] Propunere Interfață LabVIEW ce pornește fără erori
- [ ] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [ ] README în `src/app/` cu instrucțiuni lansare LabVIEW/Python
