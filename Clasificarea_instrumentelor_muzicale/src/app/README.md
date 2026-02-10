# Instrucțiuni de Rulare

Acest modul face legătura între Rețeaua Neuronală și Interfața LabVIEW. Scriptul primește un fișier audio și returnează decizia de clasificare.

## 1. Rulare Manuală (pentru Testare și Debugging)

Folosiți această metodă pentru a verifica dacă Python funcționează corect, independent de LabVIEW.

**Pasul 1:** Deschideți un terminal în folderul rădăcină al proiectului și activați mediul virtual:

.\venv\Scripts\activate

**Pasul 2:** Rulați comanda de predicție specificând calea către un fișier audio:
# Sintaxă: python src/app/main.py "CALE_CATRE_WAV"

python src/app/main.py "data/train/chitara/chitara_sample_1.wav"

Rezultat așteptat în consolă: 
--- ANALIZA FISIER: chitara_sample_1.wav ---
REZULTATE DETALIATE:
Chitara: 85.50
Pian: 10.20
...
--------------------
FINAL DECISION: Chitara
CONFIDENCE: 85.50

## 2. Configurare în LabVIEW

Pentru a integra scriptul în diagrama LabVIEW, configurați blocul **System Exec** cu următorul șir de comandă (Command Line):

**Format Obligatoriu:**

"C:\Calea_Ta_Catre_Proiect\venv\Scripts\python.exe" "C:\Calea_Ta_Catre_Proiect\src\app\main.py" "%s"
