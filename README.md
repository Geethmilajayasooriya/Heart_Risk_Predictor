# Heart Disease Risk Predictor

A web-based application to estimate heart disease risk using a machine learning model built with Python, Flask, and scikit-learn. The system provides a professional and user-friendly interface to input patient data and predict heart disease risk percentage.


## Features

- Input patient details: Name, Age, Gender, Cholesterol, Blood Pressure, Diabetes, Smoking, and Medication
- Predict heart disease risk (%) using a trained regression model
- Professional, responsive UI using Bootstrap
- Flask backend serving predictions in real-time
- Separate results page with risk percentage display

---

Run the Flask app:

python app.py


Open the app in your browser:

http://127.0.0.1:5000/

Folder Structure
heart_disease_app/
│
├── app.py                                  # Flask backend
├── heart_risk_prediction_regression_model.sav  # Trained ML model
├── requirements.txt                        # Python dependencies
├── README.md                               # Project description
├── templates/
│   ├── patient_details.html
│   └── patient_results.html
└── static/
    ├── style.css
    └── script.js (optional)

Technologies Used

Python 3
Flask
NumPy
scikit-learn
joblib
HTML, CSS, Bootstrap 5

How It Works

User inputs patient data in the form.
Flask backend receives POST request.
The ML model (.sav file) predicts heart disease risk.
Result is displayed on a professional results page with percentage.

Author

Geethmila Jayasooriya
GitHub: https://github.com/Geethmilajayasooriya
