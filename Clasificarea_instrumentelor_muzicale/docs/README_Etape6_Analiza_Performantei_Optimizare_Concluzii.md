# README – Etapa 6: Analiza Performanței, Optimizarea și Concluzii Finale

**Disciplina:** Rețele Neuronale  
**Instituție:** POLITEHNICA București – FIIR  
**Student:** Odor Sînziana-Gabriela
**Link Repository GitHub:** https://github.com/sanzianaodor/Proiect-RN.git
**Data predării:** 22.01.2026

---
## Scopul Etapei 6

Această etapă corespunde punctelor **7. Analiza performanței și optimizarea parametrilor**, **8. Analiza și agregarea rezultatelor** și **9. Formularea concluziilor finale** din lista de 9 etape - slide 2 **RN Specificatii proiect.pdf**.

**Obiectiv principal:** Maturizarea completă a Sistemului cu Inteligență Artificială (SIA) prin optimizarea modelului RN, analiza detaliată a performanței și integrarea îmbunătățirilor în aplicația software completă.

**CONTEXT IMPORTANT:** 
- Etapa 6 **ÎNCHEIE ciclul formal de dezvoltare** al proiectului
- Aceasta este **ULTIMA VERSIUNE înainte de examen** pentru care se oferă **FEEDBACK**
- Pe baza feedback-ului primit, componentele din **TOATE etapele anterioare** pot fi actualizate iterativ

**Pornire obligatorie:** Modelul antrenat și aplicația funcțională din Etapa 5:
- Model antrenat cu metrici baseline (Accuracy ≥65%, F1 ≥0.60)
- Cele 3 module integrate și funcționale
- State Machine implementat și testat

---

## MESAJ CHEIE – ÎNCHEIEREA CICLULUI DE DEZVOLTARE ȘI ITERATIVITATE

**ATENȚIE: Etapa 6 ÎNCHEIE ciclul de dezvoltare al aplicației software!**

**CE ÎNSEAMNĂ ACEST LUCRU:**
- Aceasta este **ULTIMA VERSIUNE a proiectului înainte de examen** pentru care se mai poate primi **FEEDBACK** de la cadrul didactic
- După Etapa 6, proiectul trebuie să fie **COMPLET și FUNCȚIONAL**
- Orice îmbunătățiri ulterioare (post-feedback) vor fi implementate până la examen

**PROCES ITERATIV – CE RĂMÂNE VALABIL:**
Deși Etapa 6 încheie ciclul formal de dezvoltare, **procesul iterativ continuă**:
- Pe baza feedback-ului primit, **TOATE componentele anterioare pot și trebuie actualizate**
- Îmbunătățirile la model pot necesita modificări în Etapa 3 (date), Etapa 4 (arhitectură) sau Etapa 5 (antrenare)
- README-urile etapelor anterioare trebuie actualizate pentru a reflecta starea finală

**CERINȚĂ CENTRALĂ Etapa 6:** Finalizarea și maturizarea **ÎNTREGII APLICAȚII SOFTWARE**:

1. **Actualizarea State Machine-ului** (threshold-uri noi, stări adăugate/modificate, latențe recalculate)
2. **Re-testarea pipeline-ului complet** (achiziție → preprocesare → inferență → decizie → UI/alertă)
3. **Modificări concrete în cele 3 module** (Data Logging, RN, Web Service/UI)
4. **Sincronizarea documentației** din toate etapele anterioare

**DIFERENȚIATOR FAȚĂ DE ETAPA 5:**
- Etapa 5 = Model antrenat care funcționează
- Etapa 6 = Model OPTIMIZAT + Aplicație MATURIZATĂ + Concluzii industriale + **VERSIUNE FINALĂ PRE-EXAMEN**


**IMPORTANT:** Aceasta este ultima oportunitate de a primi feedback înainte de evaluarea finală. Profitați de ea!

---

## PREREQUISITE – Verificare Etapa 5 (OBLIGATORIU)

**Înainte de a începe Etapa 6, verificați că aveți din Etapa 5:**

- [X] **Model antrenat** salvat în `models/trained_model.h5` (sau `.pt`, `.lvmodel`)
- [X] **Metrici baseline** raportate: Accuracy ≥65%, F1-score ≥0.60
- [X] **Tabel hiperparametri** cu justificări completat
- [X] **`results/training_history.csv`** cu toate epoch-urile
- [X] **UI funcțional** care încarcă modelul antrenat și face inferență reală
- [X] **Screenshot inferență** în `docs/screenshots/inference_real.png`
- [X] **State Machine** implementat conform definiției din Etapa 4

**Dacă oricare din punctele de mai sus lipsește → reveniți la Etapa 5 înainte de a continua.**

---

## Cerințe

Completați **TOATE** punctele următoare:

1. **Minimum 4 experimente de optimizare** (variație sistematică a hiperparametrilor)
2. **Tabel comparativ experimente** cu metrici și observații (vezi secțiunea dedicată)
3. **Confusion Matrix** generată și analizată
4. **Analiza detaliată a 5 exemple greșite** cu explicații cauzale
5. **Metrici finali pe test set:**
   - **Acuratețe ≥ 70%** (îmbunătățire față de Etapa 5)
   - **F1-score (macro) ≥ 0.65**
6. **Salvare model optimizat** în `models/optimized_model.h5` (sau `.pt`, `.lvmodel`)
7. **Actualizare aplicație software:**
   - Tabel cu modificările aduse aplicației în Etapa 6
   - UI încarcă modelul OPTIMIZAT (nu cel din Etapa 5)
   - Screenshot demonstrativ în `docs/screenshots/inference_optimized.png`
8. **Concluzii tehnice** (minimum 1 pagină): performanță, limitări, lecții învățate

#### Tabel Experimente de Optimizare

Documentați **minimum 4 experimente** cu variații sistematice:

| **Exp#** | **Modificare față de Baseline (Etapa 5)** | **Accuracy** | **F1-score** | **Timp antrenare** | **Observații** |
|----------|------------------------------------------|--------------|--------------|-------------------|----------------|
| Baseline | Configurația din Etapa 5 | 0.72 | 0.68 | 15 min | Referință |
| Exp 1 | Learning rate 0.0001 → 0.001 | 0.74 | 0.70 | 12 min | Convergență mai rapidă |
| Exp 2 | Batch size 32 → 64 | 0.71 | 0.67 | 10 min | Stabilitate redusă |
| Exp 3 | +1 hidden layer (128 neuroni) | 0.76 | 0.73 | 22 min | Îmbunătățire semnificativă |
| Exp 4 | Dropout 0.3 → 0.5 | 0.73 | 0.69 | 16 min | Reduce overfitting |
| Exp 5 | Augmentări domeniu (zgomot gaussian) | 0.78 | 0.75 | 25 min | **BEST** - ales pentru final |

**Justificare alegere configurație finală:**
```
Am ales Exp 5 ca model final pentru că:
1. Oferă cel mai bun F1-score (0.75), critic pentru aplicația noastră de [descrieți]
2. Îmbunătățirea vine din augmentări relevante domeniului industrial (zgomot gaussian 
   calibrat la nivelul real de zgomot din mediul de producție: SNR ≈ 20dB)
3. Timpul de antrenare suplimentar (25 min) este acceptabil pentru beneficiul obținut
4. Testare pe date noi arată generalizare bună (nu overfitting pe augmentări)
```

**Resurse învățare rapidă - Optimizare:**
- Hyperparameter Tuning: https://keras.io/guides/keras_tuner/ 
- Grid Search: https://scikit-learn.org/stable/modules/grid_search.html
- Regularization (Dropout, L2): https://keras.io/api/layers/regularization_layers/

---

## 1. Actualizarea Aplicației Software în Etapa 6 

**CERINȚĂ CENTRALĂ:** Documentați TOATE modificările aduse aplicației software ca urmare a optimizării modelului.

### Tabel Modificări Aplicație Software

| **Componenta** | **Stare Etapa 5** | **Modificare Etapa 6** | **Justificare** |
|----------------|-------------------|------------------------|-----------------|
| **Model încărcat** | `trained_model.h5` | `optimized_model.h5` | +9% accuracy, -5% FN |
| **Threshold alertă (State Machine)** | 0.5 (default) | 0.35 (clasa 'defect') | Minimizare FN în context industrial |
| **Stare nouă State Machine** | N/A | `CONFIDENCE_CHECK` | Filtrare predicții cu confidence <0.6 |
| **Latență target** | 100ms | 50ms (ONNX export) | Cerință timp real producție |
| **UI - afișare confidence** | Da/Nu simplu | Bară progres + valoare % | Feedback operator îmbunătățit |
| **Logging** | Doar predicție | Predicție + confidence + timestamp | Audit trail complet |
| **Web Service response** | JSON minimal | JSON extins + metadata | Integrare API extern |

**Completați pentru proiectul vostru:**
```markdown
### Modificări concrete aduse în Etapa 6:

1. **Model înlocuit:** `models/trained_model.h5` → `models/optimized_model.h5`
   - **Îmbunătățire:** Accuracy **82% → 99.2%**, F1-Score **0.79 → 0.99**
   - **Motivație:** Modelul optimizat integrează augmentarea datelor (rezistență la zgomot) și regularizarea L2 + Dropout (prevenire overfitting), fiind singurul capabil să distingă corect instrumentele în condiții reale, nu doar pe date ideale.

2. **State Machine actualizat:**
   - **Threshold modificat:** 0.0 (Implicit) → **0.60 (60%)**
   - **Stare nouă adăugată:** `UNCERTAIN` (Incert) - Se activează când niciun instrument nu depășește pragul de 60% încredere.
   - **Tranziție modificată:** Dacă `Confidence < Threshold` → Sistemul nu mai afișează o predicție greșită, ci rămâne în starea de așteptare (sau afișează "Zgomot/Necunoscut").

3. **UI îmbunătățit:**
   - Adăugare afișaj grafic pentru **Scorul de Încredere (Confidence Bar)**.
   - Integrare feedback vizual: titlu actualizat "Optimized v2" și avertizări pentru fișiere neconforme.
   - Screenshot: `docs/screenshots/ui_optimized.png`

4. **Pipeline end-to-end re-testat:**
   - **Flux nou:** Input Audio → **StandardScaler (Normalizare)** → MFCC → CNN Optimizat → Softmax → Threshold Check → Output.
   - **Timp total:** **~45 ms** (vs ~30 ms în Etapa 5). Creșterea este neglijabilă și justificată de pasul suplimentar de scalare care garantează precizia.


## 2. Analiza Detaliată a Performanței

### 2.1 Confusion Matrix și Interpretare

**Locație:** `docs/confusion_matrix_optimized.png`

**Analiză obligatorie (completați):**

```markdown
### Interpretare Confusion Matrix:

**Clasa cu cea mai bună performanță:** **Tobe**
- **Precision:** 100%
- **Recall:** 100%
- **Explicație:** Această clasă este cea mai distinctă din punct de vedere spectral. Sunetele percusive generează linii verticale clare pe spectrogramă și au un atac foarte rapid, spre deosebire de instrumentele melodice (Pian, Chitară, Vioară) care au armonici susținute (linii orizontale). Rețeaua CNN învață extrem de ușor aceste pattern-uri unice.

**Clasa cu cea mai slabă performanță:** **Chitară**
- **Precision:** 96%
- **Recall:** 95%
- **Explicație:** Chitara prezintă cea mai mare rată de confuzie, fiind clasa cea mai dificilă de izolat perfect. Anvelopa sunetului (ADSR) este foarte similară cu cea a pianului, mai ales în registrul mediu de frecvențe, iar în prezența zgomotului de fond adăugat (Stress Test), detaliile fine care diferențiază "ciupitura" corzii de "lovitura" ciocănelului pianului se pot pierde.

**Confuzii principale:**
1. **Clasa [Chitară] confundată cu clasa [Vioară] în ~4% din cazuri**
   - **Cauză:** Suprapunerea armonică (Spectral Overlap). Ambele sunt instrumente cu coarde, iar notele individuale fără efecte distincte (distors, reverb) au o semnătură MFCC aproape identică în primele milisecunde ale sunetului.
   - **Impact industrial:** În aplicațiile de transcriere automată a muzicii, acest lucru ar putea duce la scrierea partiturii pentru instrumentul greșit în pasajele solo simple.
   


### 2.2 Analiza Detaliată a Exemplelor Greșite

În urma rulării testelor de stres (la un nivel de zgomot ridicat de 0.85), s-a identificat o singură eroare de clasificare în eșantionul analizat, restul predicțiilor fiind corecte. 

| **Index** | **True Label** | **Predicted** | **Confidence** | **Cauză probabilă** | **Soluție propusă** |
|:---|:---|:---|:---|:---|:---|
| **chitara_10.wav** | **Chitară** | **Vioară** | ~0.55* | **Mascarea Atacului:** La un nivel de zgomot de 0.85, "ciupitura" specifică chitarei (atacul sunetului) a fost mascată. Partea de susținere a notei (*sustain*) are armonici similare cu vioara, păcălind rețeaua. | Augmentare specifică cu zgomot impulsiv la antrenare pentru a forța modelul să distingă mai clar atacul percusiv al chitarei față de atacul lent al viorii. |


```

**Analiză detaliată per exemplu (scrieți pentru fiecare):**
```markdown

### Exemplu #chitara_10.wav - Chitară clasificată ca Vioară

**Input characteristics:** Semnal audio cu raport Semnal-Zgomot (SNR) foarte scăzut. 

**Output RN:** [Vioara: ~0.55, Chitara: ~0.40, Pian: 0.05, Tobe: 0.00]

**Analiză:**
Sunetul de chitară este definit de două componente spectrale majore: atacul percusiv (tranzitoriu) și rezonanța (sustain). Zgomotul puternic de la nivelul 0.85 a "îngropat" atacul percusiv. Rețeaua CNN a analizat preponderent partea de *sustain*, care conține armonici (linii orizontale pe spectrograma MFCC) foarte similare cu cele ale viorii. Lipsind informația clară de "ciupire", modelul a ales eronat clasa cu cea mai apropiată structură armonică: Vioara.

**Implicație industrială:**
Această eroare (confuzie între instrumente cu coarde) apare doar în medii extrem de zgomotoase. Într-o aplicație reală de transcriere muzicală, ar putea duce la asignarea partiturii unui instrument greșit.

**Soluție:**
1. **Augmentare specifică:** Antrenarea modelului cu zgomot impulsiv (pocnituri scurte) suprapus peste chitară, pentru a forța rețeaua să identifice atacul corzii chiar și în condiții dificile.
2. **Denoising:** Aplicarea unui filtru de reducere a zgomotului (ex: Spectral Gating) în etapa de Preprocesare, înainte de calculul MFCC.

---

## 3. Optimizarea Parametrilor și Experimentare

### 3.1 Strategia de Optimizare

Descrieți strategia folosită pentru optimizare:

Strategia de optimizare a vizat eliminarea fenomenului de *overfitting* prin intervenții simultane la nivelul datelor și al arhitecturii. Procesul a început cu normalizarea distribuției coeficienților MFCC folosind `StandardScaler` pentru stabilizarea gradientului, urmată de augmentarea dinamică a datelor prin injecție de zgomot Gaussian și decalaj temporal (*Time Shifting*), forțând astfel modelul să învețe trăsături robuste în loc să memoreze exemplele. Suplimentar, am rafinat arhitectura rețelei prin integrarea regularizării L2 și a straturilor de Dropout progresiv (până la 50%), iar procesul de antrenare a fost controlat printr-un *Learning Rate Scheduler* care a ajustat automat rata de învățare în momentele de stagnare, asigurând convergența către performanța finală de 99%.

```markdown

### Strategie de optimizare adoptată:

**Abordare:** Tuning Manual Iterativ (Iterative Manual Tuning)

**Axe de optimizare explorate:**
1. **Arhitectură:** Extinderea de la 1 la 3 blocuri convoluționale (filtru 32 → 64 → 128) și adăugarea unui strat Dense intermediar de 128 neuroni pentru extragerea trăsăturilor complexe.
2. **Regularizare:** Implementarea **Dropout Progresiv** (creștere de la 0.2 la 0.5 spre straturile finale), **BatchNormalization** după fiecare convoluție și **L2 Regularization** (0.001) pe stratul Dense.
3. **Learning rate:** Implementarea unui scheduler dinamic (`ReduceLROnPlateau`), care reduce rata de învățare cu un factor de 0.5 după 4 epoci de stagnare a `val_loss`.
4. **Augmentări:** Augmentare online specifică domeniului audio: **Gaussian Noise Injection** (pentru robustețe la zgomot) și **Time Shifting** (pentru invarianță la poziția semnalului).
5. **Batch size:** Menținut la valoarea 16 pentru a asigura o generalizare mai bună (efect de regularizare intrinsecă) pe setul de date de dimensiuni reduse.

**Criteriu de selecție model final:** Maximizarea F1-score (>0.95) simultan cu eliminarea overfitting-ului (convergența curbelor Loss de antrenare și validare).

**Buget computațional:** ~5 experimente principale, cu un timp total de antrenare cumulat de aproximativ 90 minute.
```

### 3.2 Grafice Comparative

Generați și salvați în `docs/optimization/`:
- `accuracy_comparison.png` - Accuracy per experiment
- `f1_comparison.png` - F1-score per experiment
- `learning_curves_best.png` - Loss și Accuracy pentru modelul final

### 3.3 Raport Final Optimizare

```markdown
### Raport Final Optimizare

**Model baseline (Etapa 5):**
- Accuracy: 0.82
- F1-score: 0.79
- Latență: ~30ms (fără preprocesare avansată)

**Model optimizat (Etapa 6):**
- Accuracy: 0.9688
- F1-score: 0.9692
- Latență: ~45ms 

**Configurație finală aleasă:**
- Arhitectură: CNN Secvențial (3 blocuri Conv2D: 32, 64, 128 filtre) + Dense 128
- Learning rate: 0.001 (Adam) cu `ReduceLROnPlateau` (factor 0.5, patience 4)
- Batch size: 16
- Regularizare: L2 (0.001) pe stratul Dense + Dropout Progresiv (0.2 → 0.5) + BatchNorm
- Augmentări: Gaussian Noise Injection (zgomot) + Time Shifting (decalaj temporal)
- Epoci: 60 (Early Stopping activat, oprire tipică în jurul epocii 25-30)

**Îmbunătățiri cheie:**
1. **Integrare StandardScaler:** Normalizarea datelor a stabilizat gradientul și a eliminat blocajele de la antrenare → **+10% Accuracy**.
2. **Augmentare (Noise + Shift):** A forțat modelul să nu memoreze fișierele curate, ci să învețe caracteristici robuste → **+5% Accuracy și generalizare**.
3. **Regularizare (L2 + Dropout):** A redus drastic diferența dintre Train Loss și Validation Loss (overfitting) → **Convergență stabilă**.
```

---

## 4. Agregarea Rezultatelor și Vizualizări

### 4.1 Tabel Sumar Rezultate Finale

| **Metrică** | **Etapa 4** | **Etapa 5**  | **Etapa 6** | **Target Industrial** | **Status** |
|:---|:---|:---|:---|:---|:---|
| **Accuracy** | ~25%  | 82% | **99.2%** | ≥ 90% | Depășit |
| **F1-score (macro)** | ~0.22 | 0.79 | **0.99** | ≥ 0.85 |  Depășit |
| **Precision (Macro Avg)** | N/A | 0.80 | **0.99** | ≥ 0.90 | Depășit |
| **Recall (Macro Avg)** | N/A | 0.78 | **0.99** | ≥ 0.90 | Depășit |
| **Rata de Eroare** | ~75% | 18% | **< 1%** | ≤ 5% | Depășit |
| **Latență inferență** | - | ~30ms | **~45ms*** | ≤ 100ms | OK |
| **Throughput** | - | ~33 inf/s | **~22 inf/s** | ≥ 20 inf/s | OK |


### 4.2 Vizualizări Obligatorii

Salvați în `docs/results/`:

- [X] `confusion_matrix_optimized.png` - Confusion matrix model final
- [X] `learning_curves_final.png` - Loss și accuracy vs. epochs
- [X] `metrics_evolution.png` - Evoluție metrici Etapa 4 → 5 → 6
- [X] `example_predictions.png` - Grid cu 9+ exemple (correct + greșite)

---

## 5. Concluzii Finale și Lecții Învățate

**NOTĂ:** Pe baza concluziilor formulate aici și a feedback-ului primit, este posibil și recomandat să actualizați componentele din etapele anterioare (3, 4, 5) pentru a reflecta starea finală a proiectului.

### 5.1 Evaluarea Performanței Finale

```markdown
### Evaluare sintetică a proiectului

**Obiective atinse:**
- [X] Model RN funcțional cu accuracy [96]% pe test set
- [X] Integrare completă în aplicație software (3 module)
- [X] State Machine implementat și actualizat
- [X] Pipeline end-to-end testat și documentat
- [X] UI demonstrativ cu inferență reală
- [X] Documentație completă pe toate etapele

**Obiective parțial atinse:**
- [x] **Robustețe la zgomot extrem:** Deși modelul performează bine în condiții normale, la testele de stres cu zgomot > 0.80 s-a observat pierderea capacității de a distinge atacul sunetului ("transient"), ducând la confuzii punctuale între Chitară și Vioară.

**Obiective neatinse:**
- [X] **Extinderea diversității instrumentelor:** Proiectul s-a limitat la 4 clase principale (Chitară, Pian, Vioară, Tobe). Nu s-a reușit includerea instrumentelor de suflat (Saxofon, Flaut) din cauza lipsei de date de calitate în timpul alocat.
- [X] **Deployment pe sisteme embedded:** Optimizarea pentru rulare pe Raspberry Pi sau conversia la TensorFlow Lite (pentru mobil) a rămas la stadiul de propunere ("Future Work"), aplicația rulând momentan doar pe PC.

### 5.2 Limitări Identificate

```markdown
### Limitări tehnice ale sistemului

1. **Limitări date:**
   - **Bias către înregistrări de studio:** Dataset-ul predominant conține sunete curate, fără reverberații naturale de sală sau zgomot de fond complex (trafic, voci), ceea ce poate afecta performanța în scenarii "live" necontrolate.
   - **Diversitate limitată a stilurilor:** Datele acoperă stilurile de bază, dar lipsesc tehnici avansate de interpretare (ex: *Palm Mute* la chitară sau *Pizzicato* la vioară), care schimbă drastic amprenta spectrală.

2. **Limitări model:**
   - **Dependența de "Atac" (Transient):** Modelul se bazează puternic pe primele milisecunde ale sunetului (atacul). Dacă acest atac este mascat de zgomot (așa cum s-a văzut în Stress Test la SNR scăzut), modelul confundă instrumentele cu coarde (Chitară $\leftrightarrow$ Vioară).
   - **Confuzii pe note singulare:** Modelul performează mai slab pe note izolate în registrul mediu (400-600Hz) comparativ cu acorduri complexe, din cauza suprapunerii armonicelor între pian și chitară.

3. **Limitări infrastructură:**
   - **Portabilitate redusă:** Sistemul rulează momentan într-un mediu Python complet pe PC. Nu este optimizat (quantization) pentru rulare pe dispozitive mobile sau microcontrollere (ex: ESP32/Raspberry Pi) cu resurse limitate.
   - **Latență de preprocesare:** Deși inferența este rapidă, pasul de încărcare `librosa` și calculare MFCC adaugă o latență de ~45ms, ceea ce este acceptabil pentru clasificare, dar insuficient pentru aplicații de procesare audio în timp real (care necesită <10ms).

4. **Limitări validare:**
   - **Zgomot sintetic vs. Real:** Testele de stres au folosit zgomot Gaussian (alb). Validarea nu a acoperit tipuri de zgomot impulsiv real (ex: microfon lovit, aplauze) care ar putea genera tranzienți falși interpretați ca "Tobe".
   - **Testare pe echipamente High-End:** Validarea s-a făcut folosind fișiere audio standardizate; nu s-a testat extensiv comportamentul pe microfoane de laptop/telefon cu răspuns în frecvență slab (tăiere sub 100Hz și peste 10kHz).
```

### 5.3 Direcții de Cercetare și Dezvoltare

```markdown
### Direcții viitoare de dezvoltare

**Pe termen scurt (1-3 luni):**

1. Colectare a peste 200 de eșantioane audio adiționale pentru instrumentele care prezintă confuzie în matricea de confuzie curentă (ex: între chitară și pian).
2. Implementare Mel-Spectrograms în locul coeficienților MFCC (13 caracteristici actuale) pentru a capta o reprezentare vizuală mai bogată a spectrului armonic, îmbunătățind astfel rata de recunoaștere (Recall).
3. Optimizare latență prin conversia modelului .h5 în format TensorFlow Lite (TFLite), reducând timpul de procesare în LabVIEW pentru a permite analize pe fluxuri audio live, nu doar pe fișiere pre-înregistrate.
...

**Pe termen mediu (3-6 luni):**

1. Integrare cu stații de lucru audio digitale (DAW) prin crearea unui plugin VST care să utilizeze Web Service-ul LabVIEW pentru etichetarea automată a pistelor audio în producția muzicală.
2. Deployment pe platforme Edge (ex: NVIDIA Jetson sau Raspberry Pi) pentru a transforma proiectul într-un dispozitiv hardware portabil, independent de un PC, capabil să identifice instrumentele dintr-o sală de repetiții.
3. Implementare monitoring MLOps prin stocarea automată a fișierelor clasificate cu încredere scăzută (Confidence < 70%) într-un folder separat pentru re-antrenare (Active Learning), asigurând auto-îmbunătățirea modelului în timp.
...

```

### 5.4 Lecții Învățate

```markdown
### Lecții învățate pe parcursul proiectului

**Tehnice:**
1. Utilizarea `StandardScaler` pe caracteristicile MFCC a fost decisivă pentru convergența modelului; fără normalizare, gradientul rețelei neurale rămânea instabil.
2. Implementarea tehnicilor de **Time Shift** și **Gaussian Noise** direct în scriptul de optimizare a crescut capacitatea modelului de a clasifica corect sunete capturate în medii ne-ideale.
3. Configurarea terminalelor de ieșire ca "Stream" în LabVIEW Web Service este critică; setările implicite pot duce la răspunsuri goale de tip `{}` în browser, deși modelul rulează corect.

**Proces:**
1. Menținerea unui mediu virtual izolat și populat corect (`tensorflow`, `librosa`) este singura metodă de a asigura portabilitatea între execuția manuală în terminal și apelul automat din LabVIEW.
2. Testarea logică în `Interfata.vi` înainte de implementarea în Web Service a economisit zeci de ore de depanare a erorilor de comunicare HTTP.
3. Spațiile în numele folderelor (`an 3`, `sem 1`) pot bloca interpretorul Python; mutarea proiectului în `C:\Clasificarea_instrumentelor_muzicale` a fost soluția pentru stabilitatea executabilului.

**Colaborare:**
1. Utilizarea tab-ului *Network* și a consolei din browser a permis identificarea rapidă a erorilor de referință (`data is not defined`) în interfața HTML.
2. Scrierea rezultatelor intermediare în `debug_log.txt` a facilitat înțelegerea modului în care LabVIEW preia textul JSON de la scriptul Python.
```


### 5.5 Plan Post-Feedback (ULTIMA ITERAȚIE ÎNAINTE DE EXAMEN)

```markdown
### Plan de acțiune după primirea feedback-ului

**ATENȚIE:** Etapa 6 este ULTIMA VERSIUNE pentru care se oferă feedback!
Implementați toate corecțiile înainte de examen.

După primirea feedback-ului de la evaluatori, voi:

1. **Dacă se solicită îmbunătățiri model:**
   - Testarea unor arhitecturi de tip CRNN (Convolutional Recurrent Neural Networks) pentru captarea dependențelor temporale ale sunetului.
   - Colectarea de eșantioane audio suplimentare pentru clasele cu rată de recunoaștere scăzută (ex: chitară vs. pian).
   - **Actualizare:** `models/`, `results/`, README Etapa 5 și 6.

2. **Dacă se solicită îmbunătățiri date/preprocesare:**
   - Trecerea de la 13 coeficienți MFCC la Mel-Spectrograms (reprezentare 2D) pentru o analiză spectrală mai fină.
   - Implementarea augmentărilor de tip Pitch Shifting și Time Stretching pentru a crește variabilitatea setului de date.
   - **Actualizare:** `data/`, `src/preprocessing/`, README Etapa 3.

3. **Dacă se solicită îmbunătățiri arhitectură/State Machine:**
   - Rafinarea stărilor de eroare în `Interfata.vi` pentru gestionarea excepțiilor returnate de interpretorul Python.
   - Optimizarea funcției asincrone `scan` din `app.html` pentru a preveni blocarea interfeței în timpul procesării.
   - **Actualizare:** `docs/state_machine.*`, `src/app/`, README Etapa 4.

4. **Dacă se solicită îmbunătățiri documentație:**
   - Detalierea procesului de comunicare prin `Standard Output` între Web Service-ul LabVIEW și scriptul Python.
   - Adăugarea diagramelor de secvență pentru fluxul de date de la selectarea fișierului `.wav` până la afișarea rezultatului.
   - **Actualizare:** README-urile etapelor vizate.

5. **Dacă se solicită îmbunătățiri cod:**
   - Refactorizarea scriptului `optimize.py` prin separarea logicii de antrenare de cea de generare a graficelor.
   - Adăugarea testelor unitare pentru validarea corectitudinii extragerii caracteristicilor audio.
   - **Actualizare:** `src/`, `requirements.txt`.

**Timeline:** Implementare corecții până la data examen
**Commit final:** `"Versiune finală examen - toate corecțiile implementate"`
**Tag final:** `git tag -a v1.0-final-exam -m "Versiune finală pentru examen"`
```
---

## Structura Repository-ului la Finalul Etapei 6

**Structură COMPLETĂ și FINALĂ:**

```
proiect-rn-[prenume-nume]/
├── README.md                               # Overview general proiect (FINAL)
├── etapa3_analiza_date.md                  # Din Etapa 3
├── etapa4_arhitectura_sia.md               # Din Etapa 4
├── etapa5_antrenare_model.md               # Din Etapa 5
├── etapa6_optimizare_concluzii.md          # ← ACEST FIȘIER (completat)
│
├── docs/
│   ├── state_machine.png                   # Din Etapa 4
│   ├── state_machine_v2.png                # NOU - Actualizat (dacă modificat)
│   ├── loss_curve.png                      # Din Etapa 5
│   ├── confusion_matrix_optimized.png      # NOU - OBLIGATORIU
│   ├── results/                            # NOU - Folder vizualizări
│   │   ├── metrics_evolution.png           # NOU - Evoluție Etapa 4→5→6
│   │   ├── learning_curves_final.png       # NOU - Model optimizat
│   │   └── example_predictions.png         # NOU - Grid exemple
│   ├── optimization/                       # NOU - Grafice optimizare
│   │   ├── accuracy_comparison.png
│   │   └── f1_comparison.png
│   └── screenshots/
│       ├── ui_demo.png                     # Din Etapa 4
│       ├── inference_real.png              # Din Etapa 5
│       └── inference_optimized.png         # NOU - OBLIGATORIU
│
├── data/                                   # Din Etapa 3-5 (NESCHIMBAT)
│   ├── raw/
│   ├── generated/
│   ├── processed/
│   ├── train/
│   ├── validation/
│   └── test/
│
├── src/
│   ├── data_acquisition/                   # Din Etapa 4
│   ├── preprocessing/                      # Din Etapa 3
│   ├── neural_network/
│   │   ├── model.py                        # Din Etapa 4
│   │   ├── train.py                        # Din Etapa 5
│   │   ├── evaluate.py                     # Din Etapa 5
│   │   └── optimize.py                     # NOU - Script optimizare/tuning
│   └── app/
│       └── main.py                         # ACTUALIZAT - încarcă model OPTIMIZAT
│
├── models/
│   ├── untrained_model.h5                  # Din Etapa 4
│   ├── trained_model.h5                    # Din Etapa 5
│   ├── optimized_model.h5                  # NOU - OBLIGATORIU
│
├── results/
│   ├── training_history.csv                # Din Etapa 5
│   ├── test_metrics.json                   # Din Etapa 5
│   ├── optimization_experiments.csv        # NOU - OBLIGATORIU
│   ├── final_metrics.json                  # NOU - Metrici model optimizat
│
├── config/
│   ├── preprocessing_params.pkl            # Din Etapa 3
│   └── optimized_config.yaml               # NOU - Config model final
│
├── requirements.txt                        # Actualizat
└── .gitignore
```

**Diferențe față de Etapa 5:**
- Adăugat `etapa6_optimizare_concluzii.md` (acest fișier)
- Adăugat `docs/confusion_matrix_optimized.png` - OBLIGATORIU
- Adăugat `docs/results/` cu vizualizări finale
- Adăugat `docs/optimization/` cu grafice comparative
- Adăugat `docs/screenshots/inference_optimized.png` - OBLIGATORIU
- Adăugat `models/optimized_model.h5` - OBLIGATORIU
- Adăugat `results/optimization_experiments.csv` - OBLIGATORIU
- Adăugat `results/final_metrics.json` - metrici finale
- Adăugat `src/neural_network/optimize.py` - script optimizare
- Actualizat `src/app/main.py` să încarce model OPTIMIZAT

---

## Instrucțiuni de Rulare (Etapa 6)

### 1. Rulare experimente de optimizare

```bash
# Opțiunea A - Manual (minimum 4 experimente)
python src/neural_network/train.py --lr 0.001 --batch 32 --epochs 100 --name exp1
python src/neural_network/train.py --lr 0.0001 --batch 32 --epochs 100 --name exp2
python src/neural_network/train.py --lr 0.001 --batch 64 --epochs 100 --name exp3
python src/neural_network/train.py --lr 0.001 --batch 32 --dropout 0.5 --epochs 100 --name exp4
```

### 2. Evaluare și comparare

```bash
python src/neural_network/evaluate.py --model models/optimized_model.h5 --detailed

# Output așteptat:
# Test Accuracy: 0.8123
# Test F1-score (macro): 0.7734
# ✓ Confusion matrix saved to docs/confusion_matrix_optimized.png
# ✓ Metrics saved to results/final_metrics.json
# ✓ Top 5 errors analysis saved to results/error_analysis.json
```

### 3. Actualizare UI cu model optimizat

```bash
# Verificare că UI încarcă modelul corect
streamlit run src/app/main.py

# În consolă trebuie să vedeți:
# Loading model: models/optimized_model.h5
# Model loaded successfully. Accuracy on validation: 0.8123
```

### 4. Generare vizualizări finale

```bash
python src/neural_network/visualize.py --all

# Generează:
# - docs/results/metrics_evolution.png
# - docs/results/learning_curves_final.png
# - docs/optimization/accuracy_comparison.png
# - docs/optimization/f1_comparison.png
```

---

## Checklist Final – Bifați Totul Înainte de Predare

### Prerequisite Etapa 5 (verificare)
- [X] Model antrenat există în `models/trained_model.h5`
- [X] Metrici baseline raportate (Accuracy ≥65%, F1 ≥0.60)
- [X] UI funcțional cu model antrenat
- [X] State Machine implementat

### Optimizare și Experimentare
- [X] Minimum 4 experimente documentate în tabel
- [X] Justificare alegere configurație finală
- [X] Model optimizat salvat în `models/optimized_model.h5`
- [X] Metrici finale: **Accuracy ≥70%**, **F1 ≥0.65**
- [X] `results/optimization_experiments.csv` cu toate experimentele
- [X] `results/final_metrics.json` cu metrici model optimizat

### Analiză Performanță
- [X] Confusion matrix generată în `docs/confusion_matrix_optimized.png`
- [X] Analiză interpretare confusion matrix completată în README
- [ ] Minimum 5 exemple greșite analizate detaliat
- [X] Implicații industriale documentate (cost FN vs FP)

### Actualizare Aplicație Software
- [X] Tabel modificări aplicație completat
- [X] UI încarcă modelul OPTIMIZAT (nu cel din Etapa 5)
- [X] Screenshot `docs/screenshots/inference_optimized.png`
- [X] Pipeline end-to-end re-testat și funcțional
- [ ] (Dacă aplicabil) State Machine actualizat și documentat

### Concluzii
- [X] Secțiune evaluare performanță finală completată
- [X] Limitări identificate și documentate
- [X] Lecții învățate (minimum 5)
- [X] Plan post-feedback scris

### Verificări Tehnice
- [X] `requirements.txt` actualizat
- [X] Toate path-urile RELATIVE
- [X] Cod nou comentat (minimum 15%)
- [X] `git log` arată commit-uri incrementale
- [X] Verificare anti-plagiat respectată

### Verificare Actualizare Etape Anterioare (ITERATIVITATE)
- [X] README Etapa 3 actualizat (dacă s-au modificat date/preprocesare)
- [X] README Etapa 4 actualizat (dacă s-a modificat arhitectura/State Machine)
- [X] README Etapa 5 actualizat (dacă s-au modificat parametri antrenare)
- [X] `docs/state_machine.*` actualizat pentru a reflecta versiunea finală
- [X] Toate fișierele de configurare sincronizate cu modelul optimizat

### Pre-Predare
- [X] `etapa6_optimizare_concluzii.md` completat cu TOATE secțiunile
- [X] Structură repository conformă modelului de mai sus
- [X] Commit: `"Etapa 6 completă – Accuracy=X.XX, F1=X.XX (optimizat)"`
- [X] Tag: `git tag -a v0.6-optimized-final -m "Etapa 6 - Model optimizat + Concluzii"`
- [X] Push: `git push origin main --tags`
- [X] Repository accesibil (public sau privat cu acces profesori)

---

## Livrabile Obligatorii

Asigurați-vă că următoarele fișiere există și sunt completate:

1. **`etapa6_optimizare_concluzii.md`** (acest fișier) cu:
   - Tabel experimente optimizare (minimum 4)
   - Tabel modificări aplicație software
   - Analiză confusion matrix
   - Analiză 5 exemple greșite
   - Concluzii și lecții învățate

2. **`models/optimized_model.h5`** (sau `.pt`, `.lvmodel`) - model optimizat funcțional

3. **`results/optimization_experiments.csv`** - toate experimentele
```

4. **`results/final_metrics.json`** - metrici finale:

Exemplu:
```json
{
  "model": "optimized_model.h5",
  "test_accuracy": 0.8123,
  "test_f1_macro": 0.7734,
  "test_precision_macro": 0.7891,
  "test_recall_macro": 0.7612,
  "false_negative_rate": 0.05,
  "false_positive_rate": 0.12,
  "inference_latency_ms": 35,
  "improvement_vs_baseline": {
    "accuracy": "+9.2%",
    "f1_score": "+9.3%",
    "latency": "-27%"
  }
}
```

5. **`docs/confusion_matrix_optimized.png`** - confusion matrix model final

6. **`docs/screenshots/inference_optimized.png`** - demonstrație UI cu model optimizat

---

## Predare și Contact

**Predarea se face prin:**
1. Commit pe GitHub: `"Etapa 6 completă – Accuracy=X.XX, F1=X.XX (optimizat)"`
2. Tag: `git tag -a v0.6-optimized-final -m "Etapa 6 - Model optimizat + Concluzii"`
3. Push: `git push origin main --tags`

---

**REMINDER:** Aceasta a fost ultima versiune pentru feedback. Următoarea predare este **VERSIUNEA FINALĂ PENTRU EXAMEN**!
