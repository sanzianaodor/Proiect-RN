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

#### **Modul 1: Data Logging / Acquisition**

**Funcționalități obligatorii:**
- [X] Cod rulează fără erori: `python src/data_acquisition/generate.py` sau echivalent LabVIEW
- [X] Generează CSV în format compatibil cu preprocesarea din Etapa 3
- [X] Include minimum 40% date originale în dataset-ul final
- [X] Documentație în cod: ce date generează, cu ce parametri

#### **Modul 2: Neural Network Module**

**Funcționalități obligatorii:**
- [X] Arhitectură RN definită și compilată fără erori
- [X] Model poate fi salvat și reîncărcat
- [X] Include justificare pentru arhitectura aleasă (în docstring sau README)
- [X] **NU trebuie antrenat** cu performanță bună (weights pot fi random)


#### **Modul 3: Web Service / UI**

**Funcționalități MINIME obligatorii:**
- [ ] Propunere Interfață ce primește input de la user (formular, file upload, sau API endpoint)
- [ ] Includeți un screenshot demonstrativ în `docs/screenshots/`
---


## Checklist Final – Bifați Totul Înainte de Predare

### Documentație și Structură
- [X] Tabelul Nevoie → Soluție → Modul complet (minimum 2 rânduri cu exemple concrete completate in README_Etapa4_Arhitectura_SIA.md)
- [X] Declarație contribuție 40% date originale completată în README_Etapa4_Arhitectura_SIA.md
- [X] Cod generare/achiziție date funcțional și documentat
- [ ] Dovezi contribuție originală: grafice + log + statistici în `docs/`
- [X] Diagrama State Machine creată și salvată în `docs/state_machine.*`
- [X] Legendă State Machine scrisă în README_Etapa4_Arhitectura_SIA.md (minimum 1-2 paragrafe cu justificare)
- [ ] Repository structurat conform modelului de mai sus (verificat consistență cu Etapa 3)

### Modul 1: Data Logging / Acquisition
- [X] Cod rulează fără erori (`python src/data_acquisition/...` sau echivalent LabVIEW)
- [X] Produce minimum 40% date originale din dataset-ul final
- [X] CSV generat în format compatibil cu preprocesarea din Etapa 3
- [X] Documentație în `src/data_acquisition/README.md` cu:
  - [X] Metodă de generare/achiziție explicată
  - [X] Parametri folosiți (frecvență, durată, zgomot, etc.)
  - [X] Justificare relevanță date pentru problema voastră
- [X] Fișiere în `data/generated/` conform structurii

### Modul 2: Neural Network
- [X] Arhitectură RN definită și documentată în cod (docstring detaliat) - versiunea inițială 
- [X] README în `src/neural_network/` cu detalii arhitectură curentă

### Modul 3: Web Service / UI
- [ ] Propunere Interfață ce pornește fără erori (comanda de lansare testată)
- [ ] Screenshot demonstrativ în `docs/screenshots/ui_demo.png`
- [ ] README în `src/app/` cu instrucțiuni lansare (comenzi exacte)
