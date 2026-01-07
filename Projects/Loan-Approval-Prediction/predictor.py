import joblib
import numpy as np

model = joblib.load("model.pkl")

print("\n--- Loan Approval Prediction CLI ---\n")

gender = int(input("Gender (Male=1, Female=0): "))
married = int(input("Married (Yes=1, No=0): "))
education = int(input("Education (Graduate=1, Not Graduate=0): "))
income = float(input("Applicant Income: "))
loan_amount = float(input("Loan Amount: "))
credit_history = int(input("Credit History (1=Good, 0=Bad): "))
property_area = int(input("Property Area (Urban=2, Semiurban=1, Rural=0): "))

features = np.array([[gender, married, education,
                      income, loan_amount,
                      credit_history, property_area]])

prediction = model.predict(features)

if prediction[0] == 1:
    print("\nLoan Approved")
else:
    print("\nLoan Rejected")
