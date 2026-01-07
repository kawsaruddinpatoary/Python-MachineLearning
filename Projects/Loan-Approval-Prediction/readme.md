# Loan Approval Prediction Project

## Overview
This is a project that uses LogisticRegression, a basic machine learning model to predict if a loan approval will be approved or not using some parameters taking as inputs from the user. Here main focus is applying Machine Learning so the user interaction is handled in command line interface(CLI).

---

### Flow:
1. 📓 `loan-approval-prediction.ipynb` → Train & save model
2. 🐍 `predictor.py` → Load saved model & make predictions

**Key Point:** The notebook and CLI script do NOT run together. The saved model file (`.pkl`) connects them.

---

## 🗂 Recommended Project Structure
```
loan-approval-prediction/
│
├── loan-approval-prediction.ipynb    # Training notebook
├── predictor.py          # CLI inference script
├── model.pkl               # Saved trained model
├── data/
│   └── loan_prediction.csv      # Training d
└── README.md              # Project documentation
```

---

## 🔁 How This Works (Conceptually)
```
Notebook → trains model → saves model.pkl
CLI file → loads pkl → makes prediction
```

**Important:** The notebook never needs to be running when you use the CLI.

---

## 🧠 Step-by-Step: How to Run This

### 1️⃣ Run the Notebook (ONE TIME)

Open Jupyter Notebook:
```bash
jupyter notebook
```

Inside `loan-approval-prediction.ipynb`:
- Run all cells
- At the end, you should see:
```
  model.pkl saved successfully
```

This creates the file:
```
model.pkl
```

📌 **This is the bridge between notebook and CLI.**

### 2️⃣ Run the CLI Script

From the project root directory:
```bash
python predictor.py
```

The script loads the model:
```python
model = joblib.load("model.pkl")
```


### Run:
```bash
python predictor.py
```

**Output:**
```
Prediction: Approved
```

---

## 🎯 Summary

| Aspect | Notebook | CLI Script |
|--------|----------|------------|
| **Purpose** | Train, experiment, visualize | Make predictions |
| **When to run** | Once (or when retraining) | Every time you need a prediction |
| **Output** | `model.pkl` | Prediction result |
| **User** | Data scientist | End user / application |

---

**That is the whole project, thank you!**