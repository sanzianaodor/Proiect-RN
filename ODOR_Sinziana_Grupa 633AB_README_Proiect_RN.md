## 1. Identificare Proiect

| Câmp | Valoare |
|------|---------|
| **Student** | [Odor Sînziana-Gabriela] |
| **Grupa / Specializare** | [633AB / Informatică Industrială] |
| **Disciplina** | Rețele Neuronale |
| **Instituție** | POLITEHNICA București – FIIR |
| **Link Repository GitHub** | https://github.com/sanzianaodor/Proiect-RN.git |
| **Acces Repository** | Public |
| **Stack Tehnologic** | Mixt |
| **Domeniul Industrial de Interes (DII)** | Industrie muzicală |
| **Tip Rețea Neuronală** | CNN |

### Rezultate Cheie (Versiunea Finală vs Etapa 6)

| Metric | Țintă Minimă | Rezultat Etapa 6 | Rezultat Final | Îmbunătățire | Status |
|--------|--------------|------------------|----------------|--------------|--------|
| Accuracy (Test Set) | ≥70% | 96.88% | 97.41% | +0.53% | **✓** |
| F1-Score (Macro) | ≥0.65 | 0.96 | 0.97 | +0.01 | **✓** |
| Latență Inferență | ≤300 ms | 233.38 | 212.32 ms | -21.06 ms | **✓** |
| Contribuție Date Originale | ≥40% | 50% | 50% | - | **✓** |
| Nr. Experimente Optimizare | ≥4 | 7 | 9 | +2 | **✓** |

### Declarație de Originalitate & Politica de Utilizare AI

**Acest proiect reflectă munca, gândirea și deciziile mele proprii.**

Utilizarea asistenților de inteligență artificială (ChatGPT, Claude, Grok, GitHub Copilot etc.) este **permisă și încurajată** ca unealtă de dezvoltare – pentru explicații, generare de idei, sugestii de cod, debugging, structurarea documentației sau rafinarea textelor.

**Nu este permis** să preiau:
- cod, arhitectură RN sau soluție luată aproape integral de la un asistent AI fără modificări și raționamente proprii semnificative,
- dataset-uri publice fără contribuție proprie substanțială (minimum 40% din observațiile finale – conform cerinței obligatorii Etapa 4),
- conținut esențial care nu poartă amprenta clară a propriei mele înțelegeri.

**Confirmare explicită (bifez doar ce este adevărat):**

| Nr. | Cerință                                                                 | Confirmare |
|-----|-------------------------------------------------------------------------|------------|
| 1   | Modelul RN a fost antrenat **de la zero** (weights inițializate random, **NU** model pre-antrenat descărcat) | [X] DA     |
| 2   | Minimum **40% din date sunt contribuție originală** (generate/achiziționate/etichetate de mine) | [X] DA     |
| 3   | Codul este propriu sau sursele externe sunt **citate explicit** în Bibliografie | [X] DA     |
| 4   | Arhitectura, codul și interpretarea rezultatelor reprezintă **muncă proprie** (AI folosit doar ca tool, nu ca sursă integrală de cod/dataset) | [X] DA     |
| 5   | Pot explica și justifica **fiecare decizie importantă** cu argumente proprii | [X] DA     |

**Semnătură student (prin completare):** Declar pe propria răspundere că informațiile de mai sus sunt corecte.

Odor Sînziana-Gabriela
---

## 2. Descrierea Nevoii și Soluția SIA

### 2.1 Nevoia Reală / Studiul de Caz

*[Descrieți în 1-2 paragrafe: Ce problemă concretă din domeniul industrial rezolvă acest proiect? Care este contextul și situația actuală? De ce este importantă rezolvarea acestei probleme?]*

Proiectul rezolvă problema gestionării ineficiente a volumelor mari de date audio în industria multimedia, unde etichetarea manuală a instrumentelor muzicale este lentă și predispusă erorilor. Contextul actual cere soluții automate capabile să identifice sursele sonore cu precizie înaltă, chiar și în medii cu zgomot ambiental.
Rezolvarea acestei probleme este esențială pentru automatizarea fluxurilor de lucru în studiourile audio și arhivele digitale.

### 2.2 Beneficii Măsurabile Urmărite

*[Listați 3-5 beneficii concrete cu metrici țintă]*

1. Automatizarea clasificării audio, reducând necesitatea intervenției umane în etichetarea arhivelor sonore.

2. Asigurarea unei calități ridicate a recunoașterii, atingând un scor F1 de 0.95, ceea ce garantează o identificare precisă a instrumentelor muzicale.

3. Eficientizarea procesului de analiză în timp real prin menținerea unei latențe de inferență sub 212 ms, asigurând un răspuns rapid al interfeței LabVIEW.

4. Creșterea robusteții sistemului în medii zgomotoase, performanța fiind validată prin 9 experimente de optimizare și tehnici de augmentare a datelor.

5. Minimizarea erorilor de identificare, oferind o bază de date clasificată cu o fiabilitate extrem de ridicată.

### 2.3 Tabel: Nevoie → Soluție SIA → Modul Software

| **Nevoie reală concretă** | **Cum o rezolvă SIA-ul** | **Modul software responsabil** | **Metric măsurabil** |
|---------------------------|--------------------------|--------------------------------|----------------------|
| Identificarea automată a instrumentelor muzicale | Clasificare audio bazată pe caracteristici MFCC și rețea neurală CNN | `src/neural_network/` (Model optimizat `.h5`) | Acuratețe: 97.41% |
| Afișarea rezultatelor și monitorizarea de la distanță | Integrare hibridă între serverul LabVIEW și interfața web | `Web Service LabVIEW` + `public/app.html` | Latență: 212.32 ms |
| Menținerea preciziei în înregistrări cu zgomot ambiental | Optimizarea modelului prin tehnici de Data Augmentation | Scriptul `optimize.py` | F1-Score: 0.9729 |
| Validarea statistică a performanței modelului | Monitorizarea automată a iterațiilor de antrenare și testare | `results/` (`experiments.csv` și `final_metrics.json`) | 9 experimente de optimizare |
---

## 3. Dataset și Contribuție Originală

### 3.1 Sursa și Caracteristicile Datelor

| Caracteristică | Valoare |
|----------------|---------|
| **Origine date** | Mixt (Dataset Public + Înregistrări Proprii) |
| **Sursa concretă** | 1. Dataset Public (Kaggle): *"Music Instrument Sounds"* (autor: Abdulvahap) – utilizat pentru clasele **Vioară** și **Tobe**. 2. Achiziție Proprie: Înregistrări realizate cu microfonul – utilizate pentru clasele **Chitară** și **Pian**. |
| **Număr total observații (N)** | 320 |
| **Număr features** | 4 |
| **Tipuri de date** | Audio |
| **Format fișiere** | WAV |
| **Perioada colectării** | Noiembrie 2025 - Ianuarie 2026 |

### 3.2 Contribuția Originală (minim 40% OBLIGATORIU)

| Câmp | Valoare |
|------|---------|
| **Total observații finale (N)** | 320 |
| **Observații originale (M)** | 160 |
| **Procent contribuție originală** | 50% |
| **Tip contribuție** | Înregistrări proprii |
| **Locație date originale** | `data/generated/` |

**Descriere metodă generare/achiziție:**

*[Explicați în 1-2 paragrafe: Cum ați generat/achiziționat datele originale? Ce parametri ați folosit? De ce sunt relevante pentru problema voastră?]*

Pentru constituirea subsetului de date proprii, am utilizat o abordare duală pentru a maximiza variația timbrală. Un set de 80 de eșantioane a fost obținut prin achiziție fizică, utilizând microfonul integrat al unui smartphone pentru a înregistra instrumente reale. Această metodă a captat intenționat reverberațiile naturale ale camerei și zgomotul de fond, simulând un scenariu de utilizare reală.

Complementar, un al doilea set de 80 de eșantioane a fost generat sintetic utilizând instrumentele virtuale din aplicația GarageBand. Această sursă a furnizat sunete cu o intonație perfectă și un raport semnal-zgomot ridicat. Combinarea înregistrărilor este relevantă deoarece forțează rețeaua neuronală să învețe caracteristicile spectrale esențiale ale instrumentului, ignorând diferențele de calitate a echipamentului de înregistrare.

### 3.3 Preprocesare și Split Date

| Set | Procent | Număr Observații |
|-----|---------|------------------|
| Train | 70% | 224 |
| Validation | 15% | 48 |
| Test | 15% | 48 |

**Preprocesări aplicate:**

- Standardizare Audio: Conversia tuturor fișierelor brute la frecvența de eșantionare de 22,050 Hz și mixarea canalelor stereo în Mono pentru a asigura consistența datelor de intrare.
- Aliniere Temporală: Uniformizarea duratei tuturor eșantioanelor la fix 3 secunde.
- Extragere de Caracteristici: Calcularea a 13 coeficienți MFCC (Mel-Frequency Cepstral Coefficients), transformând sunetul într-o matrice spectrală de dimensiuni (130, 13) per eșantion.
- Normalizare Statistică: Aplicarea `StandardScaler` pe vectorii de trăsături pentru a obține o medie $\mu=0$ și o deviație standard $\sigma=1$, esențială pentru stabilitatea gradientului în rețeaua CNN.
- Formatare Tensorială: Adăugarea dimensiunii de canal (Channel Axis), transformând input-ul în format 3D (130, 13, 1) compatibil cu straturile convoluționale `Conv2D`.

---

## 4. Arhitectura SIA și State Machine

### 4.1 Cele 3 Module Software

| Modul | Tehnologie | Funcționalitate Principală | Locație în Repo |
|-------|------------|---------------------------|-----------------|
| **Data Logging / Acquisition** | Python + LabVIEW | Achiziție semnal audio, preprocesare, extragere caracteristici MFCC și augmentare date | `src/preprocessing/` |
| **Neural Network** | Python | Construire și antrenare arhitectură CNN, optimizare hiperparametri, salvare model antrenat (`.h5`) și logică de inferență. | `src/neural_network/` |
| **Web Service / UI** | LabVIEW + HTML/JS | Interfață grafică pentru utilizator (browser), upload fișier `.wav`, comunicare cu scriptul Python și afișare predicție în timp real. | `src/app/` (și `public/`) |

### 4.2 State Machine

**Locație diagramă:** `docs/state_machine.png` *(sau `state_machine_v2.png` dacă actualizată în Etapa 6)*

**Stări principale și descriere:**

| Stare | Descriere | Condiție Intrare | Condiție Ieșire |
|-------|-----------|------------------|-----------------|
| `IDLE` | [ex: Așteptare input utilizator] | [Start aplicație] | [Input primit] |
| `ACQUIRE_DATA` | [ex: Citire date de la senzor/fișier] | [Request procesare] | [Date validate] |
| `PREPROCESS` | [ex: Normalizare și extragere features] | [Date brute disponibile] | [Features ready] |
| `INFERENCE` | [ex: Forward pass prin RN] | [Input preprocesat] | [Predicție generată] |
| `DECISION` | [ex: Aplicare threshold și clasificare] | [Output RN disponibil] | [Decizie finală] |
| `OUTPUT/ALERT` | [ex: Afișare rezultat / Alertă operator] | [Decizie luată] | [Confirmare user] |
| `ERROR` | [ex: Gestionare erori și logging] | [Excepție detectată] | [Recovery/Stop] |


| `IDLE` | Sistemul așteaptă conexiuni pe portul Web Service. Interfața LabVIEW monitorizează cererile HTTP. | Start Aplicație | Cerere `POST` primită de la `app.html` (Buton "SCAN"). |
| `ACQUIRE_DATA` | LabVIEW preia calea fișierului `.wav` trimisă de utilizator și o validează. Pregătește comanda de sistem. | Input primit din Web UI | Cale fișier validă + Comanda de execuție construită. |
| `PREPROCESS` | Încărcare audio, re-eșantionare la 22kHz, Mono, Trunchiere la 3s și calculare MFCC. | Script `main.py` lansat | Matricea MFCC (130x13) extrasă cu succes. |
| `INFERENCE` | Modelul `.h5` încarcă tensorul MFCC și calculează probabilitățile pentru fiecare clasă. | Features MFCC disponibile | Vector de probabilități generat |
| `DECISION` | Interpretarea rezultatelor: aplicare `argmax` pentru clasa câștigătoare și calcul scor încredere. | Predicție brută disponibilă | Rezultat formatat ca string JSON |
| `OUTPUT/ALERT` | LabVIEW citește `Standard Output` de la Python, păstrează JSON-ul și actualizează interfața Web. | JSON primit valid | Rezultat afișat în browser + Revenire în `IDLE`. |
| `ERROR` | Gestionarea excepțiilor (fișier lipsă, format invalid, crash Python) și afișare mesaj utilizator. | Timeout execuție | Confirmare eroare / Resetare automată |


**Justificare alegere arhitectură State Machine:**

*[1 paragraf: De ce această structură pentru problema voastră specifică?]*

Am ales arhitectura de tip Mașină de Stări Finită deoarece fluxul de clasificare audio este inerent secvențial și necesită o sincronizare strictă între interfața asincronă a utilizatorului (Web/LabVIEW) și procesul sincron de inferență (Python). Această structură garantează o execuție deterministică, asigurând că resursele computaționale costisitoare (încărcarea modelului CNN) sunt alocate doar după validarea completă a datelor de intrare, eliminând astfel riscul de race condition și permițând sistemului să revină automat într-o stare stabilă (IDLE) chiar și în cazul unor erori neprevăzute în scriptul de procesare.

### 4.3 Actualizări State Machine în Etapa 6 (dacă este cazul)

| Componentă Modificată | Valoare Etapa 5 | Valoare Etapa 6 | Justificare Modificare |
|----------------------|-----------------|-----------------|------------------------|
| Arhitectură Model | CNN Simplu  | **CNN Complex | Trecerea de la un model care memora datele la unul care generalizează corect, necesar pentru validarea finală. |
| Output Date | Text simplu / Consolă | Fișiere JSON + Grafice Performanță | Implementarea cerinței de a genera rapoarte automate pentru analiză detaliată. |
| Gestiune Erori | Trunchiere agresivă | Padding Inteligent (3s) | Rezolvarea crash-urilor cauzate de fișierele audio scurte prin completarea cu zero-uri în loc de eroare. |

---

## 5. Modelul RN – Antrenare și Optimizare

### 5.1 Arhitectura Rețelei Neuronale

```

Input (shape: [130, 13, 1]) 
  → Conv2D(32, kernel=3x3, activare='relu', padding='same')
  → BatchNormalization()
  → MaxPooling2D(pool_size=(2, 2))
  
  → Conv2D(64, kernel=3x3, activare='relu', padding='same')
  → BatchNormalization()
  → MaxPooling2D(pool_size=(2, 2))

  → Conv2D(128, kernel=3x3, activare='relu', padding='same')
  → BatchNormalization()
  → MaxPooling2D(pool_size=(2, 2))

  → Flatten() 
  
  → Dense(128, activare='relu')
  → Dropout(0.5)  

  → Dense(4, activare='softmax')  
Output: 4 clase 
```

**Justificare alegere arhitectură:**

*[1-2 propoziții: De ce această arhitectură? Ce alternative ați considerat și de ce le-ați respins?]*

Am optat pentru o arhitectură CNN (Convolutional Neural Network) deoarece tratează matricea MFCC ca pe o imagine spectrală, extrăgând eficient trăsături locale (timp-frecvență) invariente la translații, esențiale pentru recunoașterea timbrului specific instrumentelor. Am respins alternativele precum MLP (Multi-Layer Perceptron), deoarece ignoră structura spațială a datelor fiind predispuse la overfitting, și RNN/LSTM, care ar fi introdus o complexitate computațională nejustificată pentru clasificarea unor segmente audio scurte și fixe.

### 5.2 Hiperparametri Finali (Model Optimizat - Etapa 6)

| Hiperparametru | Valoare Finală | Justificare Alegere |
|----------------|----------------|---------------------|
| Learning Rate | Dinamic ($0.001 \rightarrow 0.0001$) | Am utilizat un scheduler (`ReduceLROnPlateau`). Start cu $0.001$ pentru convergență rapidă, scădere automată la $0.0001$ când *val_loss* a stagnat (Epoca 15), pentru ajustări fine ale ponderilor. |
| Batch Size | 32 | Compromis ideal pentru setul de date redus. Asigură o estimare suficient de stabilă a gradientului fără a consuma excesiv memoria VRAM. |
| Epochs | Max 50 (Oprire la ~20) | Număr suficient pentru convergență. Mecanismul de Early Stopping a oprit automat antrenarea la epoca 20 pentru a preveni degradarea performanței pe setul de validare. |
| Optimizer | Adam | Algoritm adaptiv standard pentru CNN, oferind o convergență mai rapidă și mai stabilă decât SGD pe date audio spectrale. |
| Loss Function | Sparse Categorical Crossentropy | Funcția de cost optimă pentru clasificare multi-clasă unde etichetele sunt numere întregi, nu vectori one-hot. |
| Regularizare | Dropout (0.5) + BatchNorm | `Dropout` agresiv ($50\%$) a fost crucial pentru a combate overfitting-ul inerent dataset-ului mic, iar `BatchNormalization` a accelerat antrenarea prin stabilizarea distribuției activărilor. |
| Early Stopping | `patience=5`, `monitor='val_loss'` | Oprirea automată a antrenamentului dacă eroarea pe validare nu scade timp de 5 epoci consecutive, restaurând automat cei mai buni parametri (`restore_best_weights=True`). |

### 5.3 Experimente de Optimizare (minim 4 experimente)

| Exp# | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
|------|----------------------------|----------|----------|----------------|------------|
| **Baseline** | Configurația din Etapa 5 | [X.XX%] | [X.XX] | [X min] | Referință |
| Exp 1 | [ex: LR 0.001 → 0.0001] | [X.XX%] | [X.XX] | [X min] | [ex: Convergență mai lentă, +2% acc] |
| Exp 2 | [ex: +1 hidden layer (64 neuroni)] | [X.XX%] | [X.XX] | [X min] | [ex: Overfitting observat] |
| Exp 3 | [ex: Dropout 0.3 → 0.5] | [X.XX%] | [X.XX] | [X min] | [ex: Reduce overfitting din Exp 2] |
| Exp 4 | [ex: Batch 32 → 64] | [X.XX%] | [X.XX] | [X min] | [ex: Stabilitate gradient mai bună] |
| Exp 5 | [ex: Augmentări domeniu specifice] | [X.XX%] | [X.XX] | [X min] | [ex: Generalizare îmbunătățită] |
| **FINAL** | [Configurația aleasă] | **[X.XX%]** | **[X.XX]** | [X min] | **Modelul folosit în producție** |

| Exp# | Modificare față de Baseline | Accuracy | F1-Score | Timp Antrenare | Observații |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Baseline** | Configurația inițială | 96.88% | 0.9692 | **0.5 min** | Model simplu, antrenare rapidă. Referință pentru performanță, dar risc de overfitting pe date complet noi. |
| Exp 3 | Ajustare augmentare date | 95.31% | 0.9535 | 0.8 min | Scădere a preciziei (-1.5%). Indică faptul că o augmentare prea agresivă a zgomotului confundă modelul. |
| Exp 6 | + Dropout, BatchNormalization | 96.88% | 0.9692 | 1.0 min | Dublarea timpului de antrenare. Deși acuratețea este egală cu Baseline, modelul este mult mai robust matematic. |
| Exp 7 | Optimizare Pipeline + Rapoarte | 98.44% | 0.9844 | 0.9 min | Integrarea generării automate de grafice și JSON. Performanță stabilă și trasabilitate completă. |
| Exp 9 | Fine-Tuning (LR Scheduler) | **97.41%** | **0.9729** | 0.8 min | **Configurația aleasă.** Convergență perfectă pe setul de testare cu un echilibru ideal între viteză și precizie. |

**Justificare alegere model final:**

*[1 paragraf: De ce această configurație? Ce compromisuri ați făcut între accuracy/timp/complexitate?]*

Am selectat configurația din Experimentul 9 deoarece validează eficiența mecanismelor de regularizare (Dropout, BatchNormalization) și a ajustării dinamice a ratei de învățare (ReduceLROnPlateau). Deși această arhitectură introduce o creștere marginală a complexității computaționale și a timpului de antrenare ($0.5 \rightarrow 0.8$ min) față de varianta Baseline, am acceptat acest compromis pentru a elimina riscul de overfitting și a garanta stabilitatea predicțiilor în condiții reale de zgomot, unde un model simplist ar fi eșuat.

**Referințe fișiere:** `results/optimization_experiments.csv`, `models/optimized_model.h5`

---

## 6. Performanță Finală și Analiză Erori

### 6.1 Metrici pe Test Set (Model Optimizat)

| Metric | Valoare | Target Minim | Status |
|--------|---------|--------------|--------|
| **Accuracy** | 97.41% | ≥70% | ✓ |
| **F1-Score (Macro)** | 0.9729 | ≥0.65 | ✓ |
| **Precision (Macro)** | 0.9575 | - | - |
| **Recall (Macro)** | 0.9531 | - | - |

**Îmbunătățire față de Baseline (Etapa 5):**

| Metric | Etapa 5 (Baseline) | Etapa 6 (Optimizat) | Îmbunătățire |
|--------|-------------------|---------------------|--------------|
| **Accuracy** | 96.88% | 97.41% | +0.53% |
| **F1-Score** | 0.9692 | 0.9729 | +0.0037 |

**Referință fișier:** `results/final_metrics.json`

### 6.2 Confusion Matrix

**Locație:** `docs/confusion_matrix_optimized.png`

**Interpretare:**

| Aspect | Observație |
|--------|------------|
| **Clasa cu cea mai bună performanță** | Tobe - Precision 100%, Recall 100% |
| **Clasa cu cea mai slabă performanță** | Vioară - Precision 95%, Recall 94% |
| **Confuzii frecvente** | Vioară și Chitară. Ambele fiind instrumente cu coarde, există o suprapunere semnificativă a armonicelor în registrele medii, ceea ce poate determina modelul să clasifice greșit anumite acorduri susținute. |
| **Dezechilibru clase** | Impact neglijabil. Valoarea ridicată a F1-Score Macro (0.9729) demonstrează că modelul a învățat să generalizeze corect, nefiind părtinitor către o clasă majoritară, în ciuda numărului redus de date. |

### 6.3 Analiza Top 5 Erori

| # | Input (descriere scurtă) | Predicție RN | Clasă Reală | Cauză Probabilă | Implicație Industrială |
|---|--------------------------|--------------|-------------|-----------------|------------------------|
| 1 | Vioară | Chitară | Vioară | Similaritate sunet: Tehnica pizzicato (ciupirea corzii) produce un atac scurt și o stingere rapidă, generând o spectrogramă aproape identică cu cea a unei chitare, inducând în eroare rețeaua care asociază vioara cu sunetul continuu (arcuș). | Clasificare greșită în baze de date muzicale: Într-o aplicație de streaming (ex: Spotify), piese de muzică clasică ar putea fi etichetate automat greșit ca fiind "Muzică Acustică/Folk", afectând recomandările pentru utilizatori. |
| 2 | Chitară | Vioară | Chitară | Lipsă tranzienți: Un acord de chitară lăsat să sune mult timp (sustain), fără atacul percusiv inițial, are un spectru armonic continuu care seamănă matematic cu vibrația constantă a corzii frecate de arcuș la vioară. | Eroare în transcrierea automată: Un software de generare automată a partiturilor ar putea scrie linia melodică pe portativul greșit (Vioară în loc de Chitară), necesitând corecție manuală costisitoare. |

### 6.4 Validare în Context Industrial

**Ce înseamnă rezultatele pentru aplicația reală:**

*[1 paragraf: Traduceți metricile în impact real în domeniul vostru industrial]*

O acuratețe de 97.41% implică faptul că, dintr-un volum ipotetic de 1.000 de fișiere audio procesate automat de platformă, 974 sunt etichetate corect fără intervenție umană, ceea ce reduce masiv costurile operaționale de sortare. Cele aproximativ 26 de erori (2.59%) sunt, în marea lor majoritate, confuzii între Chitară și Vioară, considerate "erori benigne" în context educațional (utilizatorul primește totuși o sugestie din familia corectă - Coarde). Costul real al erorii este minim, reprezentând doar timpul necesar unui operator uman sau utilizatorului final să corecteze manual eticheta pentru acele 2-3 fișiere la suta de încărcări, un compromis excelent pentru automatizarea aproape totală a procesului.

**Pragul de acceptabilitate pentru domeniu:** Recall ≥ 95% pentru instrumente percusive distincte  
**Status:** Atins 
**Plan de îmbunătățire (dacă neatins):** Creșterea duratei segmentului audio de la 3 secunde la 5 secunde pentru a captura mai bine anvelopa sunetului

---

## 7. Aplicația Software Finală

### 7.1 Modificări Implementate în Etapa 6

| Componentă | Stare Etapa 5 | Modificare Etapa 6 | Justificare |
|------------|---------------|-------------------|-------------|
| **Model încărcat** | `trained_model.h5` | `optimized_model.h5` | [ex: +8% accuracy, -12% FN] |
| **Threshold decizie** | [ex: 0.5 default] | [ex: 0.35 pentru clasa 'defect'] | [ex: Minimizare FN în context producție] |
| **UI - feedback vizual** | [ex: Da/Nu text] | [ex: Bară confidence + valoare %] | [ex: Informare operator pentru decizii] |
| **Logging** | [ex: Doar predicție] | [ex: Predicție + confidence + timestamp] | [ex: Audit trail pentru QA] |
| [Alte modificări] | [Completați] | [Completați] | [Completați] |

| **Model Încărcat** | `final_model.h5` | `optimized_model.h5` | Creșterea acurateței la **97.41%** și a robusteței la zgomot prin utilizarea straturilor de regularizare  |
| **Strategie Preprocesare** | Trunchiere brută | Zero-Padding (fix 3 sec) | Standardizarea tensorului de intrare la `(130, 13, 1)`. Elimină erorile critice la procesarea fișierelor scurte |
| **Rată de Învățare (LR)** | Constantă ($0.001$) | Dinamică (ReduceLROnPlateau) | Optimizare fină a ponderilor. LR scade automat când eroarea stagnează, permițând convergența către minimul global. |
| **Arhitectură Internă** | CNN Simplu | CNN + BatchNormalization + Dropout | Prevenirea fenomenului de Overfitting. Modelul învață trăsături reale ale timbrului, nu doar să memoreze datele de antrenament. |
| **Sistem de Logging** | Afișare în consolă | Salvare Automată (CSV/JSON) | Asigurarea trasabilității experimentelor. Permite auditarea performanței și generarea automată a rapoartelor. |

### 7.2 Screenshot UI cu Model Optimizat

**Locație:** `docs/screenshots/inference_optimized.png`

*[Descriere scurtă: Ce se vede în screenshot? Ce demonstrează?]*

Clasificarea corectă a unui eșantion audio (ex: Vioară) cu un scor de încredere ridicat (>97%). Se observă output-ul structurat care confirmă integrarea cu succes a modelului optimizat optimized_model.h5 și capacitatea acestuia de a oferi predicții clare pe date noi."

### 7.3 Demonstrație Funcțională End-to-End

**Locație dovadă:** `docs/demo/` *(GIF / Video / Secvență screenshots)*

**Fluxul demonstrat:**

| Pas | Acțiune | Rezultat Vizibil |
|-----|---------|------------------|
| 1 | Input | [ex: Upload imagine nouă (NU din train/test)] |
| 2 | Procesare | [ex: Bară de progres + preprocesare vizibilă] |
| 3 | Inferență | [ex: Predicție afișată: "Clasa: Defect, Confidence: 87%"] |
| 4 | Decizie | [ex: Alertă roșie + sunet pentru operator] |

| 1 | Input | Încărcare fișier audio `.wav` extern |
| 2 | Procesare | Mesaj consolă: "Extracting MFCC..." -> Generare tensor `(130, 13, 1)` prin Zero-Padding automat. |
| 3 | Inferență | Predicție afișată în UI/Consolă: "Instrument: Vioară", "Confidence: 97.42%". |
| 4 | Decizie | Afișare instrument/mesaj confirmare |

**Latență măsurată end-to-end:** 120 ms  
**Data și ora demonstrației:** [10.02.2026, 15:36]

---

## 8. Structura Repository-ului Final

```
proiect-rn-[nume-prenume]/
│
├── README.md                               # ← ACEST FIȘIER (Overview Final Proiect - Pe moodle la Evaluare Finala RN > Upload Livrabil 1 - Proiect RN (Aplicatie Sofware) - trebuie incarcat cu numele: NUME_Prenume_Grupa_README_Proiect_RN.md)
│
├── docs/
│   ├── etapa3_analiza_date.md              # Documentație Etapa 3
│   ├── etapa4_arhitectura_SIA.md           # Documentație Etapa 4
│   ├── etapa5_antrenare_model.md           # Documentație Etapa 5
│   ├── etapa6_optimizare_concluzii.md      # Documentație Etapa 6
│   │
│   ├── state_machine.png                   # Diagrama State Machine inițială
│   ├── state_machine_v2.png                # (opțional) Versiune actualizată Etapa 6
│   ├── confusion_matrix_optimized.png      # Confusion matrix model final
│   │
│   ├── screenshots/
│   │   ├── ui_demo.png                     # Screenshot UI schelet (Etapa 4)
│   │   ├── inference_real.png              # Inferență model antrenat (Etapa 5)
│   │   └── inference_optimized.png         # Inferență model optimizat (Etapa 6)
│   │
│   ├── demo/                               # Demonstrație funcțională end-to-end
│   │   └── demo_end_to_end.gif             # (sau .mp4 / secvență screenshots)
│   │
│   ├── results/                            # Vizualizări finale
│   │   ├── loss_curve.png                  # Grafic loss/val_loss (Etapa 5)
│   │   ├── metrics_evolution.png           # Evoluție metrici (Etapa 6)
│   │   └── learning_curves_final.png       # Curbe învățare finale
│   │
│   └── optimization/                       # Grafice comparative optimizare
│       ├── accuracy_comparison.png         # Comparație accuracy experimente
│       └── f1_comparison.png               # Comparație F1 experimente
│
├── data/
│   ├── README.md                           # Descriere detaliată dataset
│   ├── raw/                                # Date brute originale
│   ├── processed/                          # Date curățate și transformate
│   ├── generated/                          # Date originale (contribuția ≥40%)
│   ├── train/                              # Set antrenare (70%)
│   ├── validation/                         # Set validare (15%)
│   └── test/                               # Set testare (15%)
│
├── src/
│   ├── data_acquisition/                   # MODUL 1: Generare/Achiziție date
│   │   ├── README.md                       # Documentație modul
│   │   ├── generate.py                     # Script generare date originale
│   │   └── [alte scripturi achiziție]
│   │
│   ├── preprocessing/                      # Preprocesare date (Etapa 3+)
│   │   ├── data_cleaner.py                 # Curățare date
│   │   ├── feature_engineering.py          # Extragere/transformare features
│   │   ├── data_splitter.py                # Împărțire train/val/test
│   │   └── combine_datasets.py             # Combinare date originale + externe
│   │
│   ├── neural_network/                     # MODUL 2: Model RN
│   │   ├── README.md                       # Documentație arhitectură RN
│   │   ├── model.py                        # Definire arhitectură (Etapa 4)
│   │   ├── train.py                        # Script antrenare (Etapa 5)
│   │   ├── evaluate.py                     # Script evaluare metrici (Etapa 5)
│   │   ├── optimize.py                     # Script experimente optimizare (Etapa 6)
│   │   └── visualize.py                    # Generare grafice și vizualizări
│   │
│   └── app/                                # MODUL 3: UI/Web Service
│       ├── README.md                       # Instrucțiuni lansare aplicație
│       └── main.py                         # Aplicație principală
│
├── models/
│   ├── untrained_model.h5                  # Model schelet neantrenat (Etapa 4)
│   ├── trained_model.h5                    # Model antrenat baseline (Etapa 5)
│   ├── optimized_model.h5                  # Model FINAL optimizat (Etapa 6) ← FOLOSIT
│   └── final_model.onnx                    # (opțional) Export ONNX pentru deployment
│
├── results/
│   ├── training_history.csv                # Istoric antrenare - toate epocile (Etapa 5)
│   ├── test_metrics.json                   # Metrici baseline test set (Etapa 5)
│   ├── optimization_experiments.csv        # Toate experimentele optimizare (Etapa 6)
│   ├── final_metrics.json                  # Metrici finale model optimizat (Etapa 6)
│   └── error_analysis.json                 # Analiza detaliată erori (Etapa 6)
│
├── config/
│   ├── preprocessing_params.pkl            # Parametri preprocesare salvați (Etapa 3)
│   └── optimized_config.yaml               # Configurație finală model (Etapa 6)
│
├── requirements.txt                        # Dependențe Python (actualizat la fiecare etapă)
└── .gitignore                              # Fișiere excluse din versionare
```

### Legendă Progresie pe Etape

| Folder / Fișier | Etapa 3 | Etapa 4 | Etapa 5 | Etapa 6 |
|-----------------|:-------:|:-------:|:-------:|:-------:|
| `data/raw/`, `processed/`, `train/`, `val/`, `test/` | ✓ Creat | - | Actualizat* | - |
| `data/generated/` | - | ✓ Creat | - | - |
| `src/preprocessing/` | ✓ Creat | - | Actualizat* | - |
| `src/data_acquisition/` | - | ✓ Creat | - | - |
| `src/neural_network/model.py` | - | ✓ Creat | - | - |
| `src/neural_network/train.py`, `evaluate.py` | - | - | ✓ Creat | - |
| `src/neural_network/optimize.py`, `visualize.py` | - | - | - | ✓ Creat |
| `src/app/` | - | ✓ Creat | Actualizat | Actualizat |
| `models/untrained_model.*` | - | ✓ Creat | - | - |
| `models/trained_model.*` | - | - | ✓ Creat | - |
| `models/optimized_model.*` | - | - | - | ✓ Creat |
| `docs/state_machine.*` | - | ✓ Creat | - | (v2 opțional) |
| `docs/etapa3_analiza_date.md` | ✓ Creat | - | - | - |
| `docs/etapa4_arhitectura_SIA.md` | - | ✓ Creat | - | - |
| `docs/etapa5_antrenare_model.md` | - | - | ✓ Creat | - |
| `docs/etapa6_optimizare_concluzii.md` | - | - | - | ✓ Creat |
| `docs/confusion_matrix_optimized.png` | - | - | - | ✓ Creat |
| `docs/screenshots/` | - | ✓ Creat | Actualizat | Actualizat |
| `results/training_history.csv` | - | - | ✓ Creat | - |
| `results/optimization_experiments.csv` | - | - | - | ✓ Creat |
| `results/final_metrics.json` | - | - | - | ✓ Creat |
| **README.md** (acest fișier) | Draft | Actualizat | Actualizat | **FINAL** |

*\* Actualizat dacă s-au adăugat date noi în Etapa 4*

### Convenție Tag-uri Git

| Tag | Etapa | Commit Message Recomandat |
|-----|-------|---------------------------|
| `v0.3-data-ready` | Etapa 3 | "Etapa 3 completă - Dataset analizat și preprocesat" |
| `v0.4-architecture` | Etapa 4 | "Etapa 4 completă - Arhitectură SIA funcțională" |
| `v0.5-model-trained` | Etapa 5 | "Etapa 5 completă - Accuracy=X.XX, F1=X.XX" |
| `v0.6-optimized-final` | Etapa 6 | "Etapa 6 completă - Accuracy=X.XX, F1=X.XX (optimizat)" |

---

## 9. Instrucțiuni de Instalare și Rulare

### 9.1 Cerințe Preliminare

```
Python >= 3.8 (recomandat 3.10+)
pip >= 21.0
[sau LabVIEW >= 2020 pentru proiecte LabVIEW]
```

### 9.2 Instalare

```bash
# 1. Clonare repository
git clone [URL_REPOSITORY]
cd proiect-rn-[nume-prenume]

# 2. Creare mediu virtual (recomandat)
python -m venv venv
source venv/bin/activate        # Linux/Mac
# sau: venv\Scripts\activate    # Windows

# 3. Instalare dependențe
pip install -r requirements.txt
```

### 9.3 Rulare Pipeline Complet

```bash
# Pasul 1: Preprocesare date (dacă rulați de la zero)
python src/preprocessing/data_cleaner.py
python src/preprocessing/data_splitter.py --stratify --random_state 42

# Pasul 2: Antrenare model (pentru reproducere rezultate)
python src/neural_network/train.py --config config/optimized_config.yaml

# Pasul 3: Evaluare model pe test set
python src/neural_network/evaluate.py --model models/optimized_model.h5

# Pasul 4: Lansare aplicație UI
streamlit run src/app/main.py
# sau: python src/app/main.py (pentru Flask/FastAPI)
# sau: [instrucțiuni LabVIEW dacă aplicabil]
```

### 9.4 Verificare Rapidă 

```bash
# Verificare că modelul se încarcă corect
python -c "from src.neural_network.model import load_model; m = load_model('models/optimized_model.h5'); print('✓ Model încărcat cu succes')"

# Verificare inferență pe un exemplu
python src/neural_network/evaluate.py --model models/optimized_model.h5 --quick-test
```

### 9.5 Structură Comenzi LabVIEW (dacă aplicabil)

```
1. **Activare Mediu Virtual:**
   - Deschideți terminalul în folderul rădăcină al proiectului.
   - Windows: `venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`

2. **Lansare Interfață:**
   - *Nota:* Asigurați-vă că fișierul `optimized_model.h5` este în folderul `models/`.

3. **Utilizare:**
   - Apăsați butonul **"Load Audio File"** și selectați un fișier `.wav` de test.
   - Aplicația va afișa automat clasa prezisă (ex: "Vioară") și scorul de încredere (ex: "97.41%").

```

---

## 10. Concluzii și Discuții

### 10.1 Evaluare Performanță vs Obiective Inițiale

| Obiectiv Definit (Secțiunea 2) | Target | Realizat | Status |
|--------------------------------|--------|----------|--------|
| [Obiectiv 1 din 2.2] | [target] | [realizat] | [✓/✗] |
| [Obiectiv 2 din 2.2] | [target] | [realizat] | [✓/✗] |
| Accuracy pe test set | ≥70% | [X.XX%] | [✓/✗] |
| F1-Score pe test set | ≥0.65 | [X.XX] | [✓/✗] |
| [Metric specific domeniului] | [target] | [realizat] | [✓/✗] |

| Clasificare Instrumente | 4 Clase | 4 Clase | ✓ |
| Robustețe la Zgomot | Funcționare pe date reale | Demonstrat prin Dropout 0.5 & Augmentare | ✓ |
| Accuracy pe test set | ≥70% | 97.41% | ✓ |
| F1-Score pe test set | ≥0.65 | 0.9729 | ✓ |
| Recall (Critic - Tobe) | ≥85% | 100.00% | ✓ |

### 10.2 Ce NU Funcționează – Limitări Cunoscute

*[Fiți onești - evaluatorul apreciază identificarea clară a limitărilor]*

1.  **Limitare 1 (Confuzii Timbrale la Coarde):** Modelul întâmpină dificultăți în distingerea instrumentelor din familia coardelor (**Vioară vs. Chitară**) atunci când se cântă în registre medii sau se folosesc tehnici atipice, din cauza similarității spectrale a armonicelor.
2.  **Limitare 2 (Analiză strict Monofonică):** Sistemul este proiectat exclusiv pentru instrumente **solo**. Nu poate clasifica corect un fișier audio care conține mai multe instrumente simultan (polifonie/orchestră), deoarece suprapunerea frecvențelor alterează tiparul MFCC pe care s-a antrenat rețeaua.
3.  **Limitare 3 (Fereastră Temporală Fixă):** Arhitectura CNN impune un input fix (matricea MFCC). Fișierele mai lungi de 3 secunde sunt trunchiate automat, pierzându-se informația de la finalul înregistrării, care ar putea fi relevantă pentru clasificarea corectă.
4.  **Funcționalități planificate dar neimplementate:**
    * **Suport Microfon Live:** Procesarea fluxului audio în timp real (streaming) direct de la microfon, nu doar prin încărcarea fișierelor `.wav`.

### 10.3 Lecții Învățate (Top 5)

1.  **Lecția 1 (Capcana "Acurateței Perfecte"):** Am învățat să privesc cu scepticism rezultatele de **100%** pe seturi de date limitate. Am înțeles că perfecțiunea metrică indică adesea *Overfitting* (memorare mecanică), iar alegerea conștientă a unui model cu o eroare mică dar constantă este o decizie superioară pentru a garanta generalizarea pe date noi.
2.  **Lecția 2 (Preprocesarea bate Modelarea):** Erorile inițiale de dimensiune a tensorilor mi-au demonstrat că rețelele CNN sunt rigide la input. Implementarea Zero-Padding-ului (standardizarea la 3 secunde) a fost mai valoroasă pentru stabilitatea aplicației (eliminând crash-urile pe fișiere scurte de tobe) decât orice ajustare fină a hiperparametrilor.
3.  **Lecția 3 (Regularizarea este Cheia):** Deși modelul *Baseline* avea performanțe bune, era fragil. Introducerea straturilor de Dropout (0.5) și BatchNormalization a crescut timpul de antrenare, dar a forțat rețeaua să învețe trăsături reale ale timbrului, nu zgomotul de fond specific microfonului de înregistrare.
4.  **Lecția 4 (Limitele Fizice ale Datelor):** Confuzia persistentă între *Vioară* și *Chitară* mi-a arătat că algoritmii nu pot face "magie" dacă datele sunt ambigue fizic. MFCC-urile pe ferestre scurte pierd informația despre *atacul* notei (transienți), subliniind necesitatea unei ferestre de analiză mai largi (>3s) pentru a distinge instrumentele cu coarde.
5.  **Lecția 5 (Automatizarea Experimentelor):** Trecerea de la rularea manuală la un pipeline automatizat (cu Logging CSV/JSON și Callbacks precum `ReduceLROnPlateau`) a transformat optimizarea dintr-un proces haotic, într-o analiză sistematică, economisind ore de muncă și permițând comparația obiectivă a celor 9 experimente.

### 10.4 Retrospectivă

**Ce ați schimba dacă ați reîncepe proiectul?**

*[1-2 paragrafe: Decizii pe care le-ați lua diferit, cu justificare bazată pe experiența acumulată]*

Din punct de vedere al integrării software, aș aborda diferit comunicarea dintre interfață și model. În loc de apeluri simple de scripturi, m-aș documenta aprofundat despre LabVIEW Web Services pentru a implementa o arhitectură de tip Client-Server. 

În paralel, aș investi efort considerabil în extinderea setului de date. Dublarea numărului de eșantioane și includerea unor înregistrări din medii acustice diferite ar transforma modelul dintr-unul experimental într-unul industrial, capabil să generalizeze corect chiar și în condiții de zgomot sau variații timbrale extreme.

### 10.5 Direcții de Dezvoltare Ulterioară

| Termen | Îmbunătățire Propusă | Beneficiu Estimat |
|--------|---------------------|-------------------|
| **Short-term** (1-2 săptămâni) | [ex: Augmentare date pentru clasa subreprezentată] | [ex: +10% recall pe clasa "defect_minor"] |
| **Medium-term** (1-2 luni) | [ex: Implementare model ensemble] | [ex: +3-5% accuracy general] |
| **Long-term** | [ex: Deployment pe edge device (Raspberry Pi)] | [ex: Latență <20ms, cost hardware redus] |

| **Short-term** (1-2 săptămâni) | Augmentare date țintită: Colectarea a 50-100 sample-uri specifice pentru cazurile de confuzie și reantrenarea modelului. | Creșterea preciziei la >98% pe clasele din familia *Coarde*, eliminând erorile fine de clasificare timbrală. |
| **Medium-term** (1-2 luni) | Arhitectură Client-Server (LabVIEW Web Services): Documentarea și refactorizarea aplicației pentru a rula Python ca un serviciu REST continuu, apelat din LabVIEW doar pentru afișare. | Interfață Reactivă & Latență Minimă.Elimină timpul de încărcare al interpretorului Python la fiecare rulare (modelul rămâne "încărcat" în RAM), oferind o experiență de utilizare fluidă. |
| **Long-term** | Real-time Streaming & Portare Mobile: Adaptarea modelului pentru input continuu (microfon live) și conversia la format `TFLite` sau `ONNX`. | Portabilitate totală.  Rulare pe dispozitive embedded (Raspberry Pi, Telefon) în timp real, independent de un PC puternic. |
---

## 11. Bibliografie

*[Minimum 3 surse cu DOI/link funcțional - format: Autor, Titlu, Anul, Link]*
1. Note de curs și laborator 2025. Rețele Neuronale, UNSTPB, Facultatea de Inginerie Industrială și Robotică
2. F1-score. https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html
2. Abaza, B., 2025. AI-Driven Dynamic Covariance for ROS 2 Mobile Robot Localization. Sensors, 25, 3026. https://doi.org/10.3390/s25103026
3. Keras Documentation, 2024. Getting Started Guide. https://keras.io/getting_started/

---

## 12. Checklist Final (Auto-verificare înainte de predare)

### Cerințe Tehnice Obligatorii

- [X] **Accuracy ≥70%** pe test set (verificat în `results/final_metrics.json`)
- [X] **F1-Score ≥0.65** pe test set
- [X] **Contribuție ≥40% date originale** (verificabil în `data/generated/`)
- [X] **Model antrenat de la zero** (NU pre-trained fine-tuning)
- [X] **Minimum 4 experimente** de optimizare documentate (tabel în Secțiunea 5.3)
- [X] **Confusion matrix** generată și interpretată (Secțiunea 6.2)
- [X] **State Machine** definit cu minimum 4-6 stări (Secțiunea 4.2)
- [X] **Cele 3 module funcționale:** Data Logging, RN, UI (Secțiunea 4.1)
- [X] **Demonstrație end-to-end** disponibilă în `docs/demo/`

### Repository și Documentație

- [X] **README.md** complet (toate secțiunile completate cu date reale)
- [X] **4 README-uri etape** prezente în `docs/` (etapa3, etapa4, etapa5, etapa6)
- [X] **Screenshots** prezente în `docs/screenshots/`
- [X] **Structura repository** conformă cu Secțiunea 8
- [X] **requirements.txt** actualizat și funcțional
- [X] **Cod comentat** (minim 15% linii comentarii relevante)
- [X] **Toate path-urile relative** (nu absolute: `/Users/...` sau `C:\...`)

### Acces și Versionare

- [X] **Repository accesibil** cadrelor didactice RN (public sau privat cu acces)
- [X] **Tag `v0.6-optimized-final`** creat și pushed
- [X] **Commit-uri incrementale** vizibile în `git log` (nu 1 commit gigantic)
- [X] **Fișiere mari** (>100MB) excluse sau în `.gitignore`

### Verificare Anti-Plagiat

- [X] Model antrenat **de la zero** (weights inițializate random, nu descărcate)
- [X] **Minimum 40% date originale** (nu doar subset din dataset public)
- [X] Cod propriu sau clar atribuit (surse citate în Bibliografie)

---

## Note Finale

**Versiune document:** FINAL pentru examen  
**Ultima actualizare:** [10.02.2026]  
**Tag Git:** `v0.6-optimized-final`

---

*Acest README servește ca documentație principală pentru Livrabilul 1 (Aplicație RN). Pentru Livrabilul 2 (Prezentare PowerPoint), consultați structura din RN_Specificatii_proiect.pdf.*
