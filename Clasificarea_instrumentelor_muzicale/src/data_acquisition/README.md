# Protocol de Achiziție a Datelor (Data Acquisition)

Acest document descrie metodologia utilizată pentru colectarea setului de date original ("Contribuție Proprie"), format din clasele **Chitară** și **Pian**.

## 1. Setup Experimental (Hardware)

* **Senzor:** Microfon [Telefon]
* **Mediu:** Mediu necontrolat acustic.
* **Poziționare:** Microfonul a fost plasat la o distanță de aproximativ 20-40 cm de sursa sonoră pentru a capta atât timbrul instrumentului, cât și reverberațiile naturale ale camerei.

## 2. Software de Captură & Generare

### A. Înregistrări Fizice (Real-World)
* **Software:** [Voice Recorder]
* **Format Brut:** .WAV 
* **Post-procesare inițială:** Fișierele au fost tăiate manual pentru a elimina secțiunile lungi de liniște înainte de a intra în pipeline-ul automat de procesare.

### B. Generare Sintetică
* **Software:** GarageBand 
* **Metodă:** Utilizarea instrumentelor virtuale pentru a genera fișiere audio
* **Scop:** Antrenarea rețelei neuronale.

## 3. Surse Externe
Pentru clasele **Tobe** și **Vioară**, s-au utilizat subseturi din dataset-uri publice (Kaggle), selectate manual pentru a corespunde calitativ cu înregistrările proprii.

## 4. Statistici Achiziție
* **Total fișiere proprii:** 160
* **Total fișiere externe:** 160
* **Distribuție:** Echilibrată (80 fișiere per clasă).