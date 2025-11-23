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

##  2. Descrierea Setului de Date

### 2.1 Sursa datelor

* **Origine:** dataset public
* **Modul de achiziție:**  Fișier extern 
* **Perioada / condițiile colectării:** Noiembrie 2024 - Ianuarie 2025, condiții experimentale specifice

### 2.2 Caracteristicile dataset-ului

* **Număr total de observații:** 80
* **Număr de caracteristici (features):** 20
* **Tipuri de date:** Sunete
* **Format fișiere:** WAV

### 2.3 Descrierea fiecărei caracteristici

| **Caracteristică** | **Tip** | **Unitate** | **Descriere** | **Domeniu valori** |
|-------------------|---------|-------------|---------------|--------------------|
| chitară | sound | - | [...] | 20 |
| pian | sound | – | [...] | 20 |
| tobe | sound | - | [...] | 20 |
| vioară | sound | - | ... | 20 |

**Fișier recomandat:**  `data/README.md`

---
