# CardioMate — Heart Risk Predictor

CardioMate is a lightweight Flask web application that provides an educational estimate of heart disease risk using a pre-trained machine-learning model.



## Highlights
- Simple, responsive UI with landing page, input form, and results page
- Accessibility and UX improvements (ARIA attributes, keyboard focus states)
- Clean branding: logo, favicon, and typography (Poppins)
- Color-coded risk badge with short explanatory guidance
- Contact modal and About section

## Quick start (local)
1. Create a virtual environment and activate it:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # Windows
   source venv/bin/activate  # macOS / Linux
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:

   ```bash
   python heart_risk_level_predictor.py
   ```

4. Open http://127.0.0.1:5000 in your browser

## Files of interest
- `heart_risk_level_predictor.py` — Flask app and routes
- `templates/` — Jinja2 templates (`welcome.html`, `patient_details.html`, `patient_results.html`)
- `static/` — CSS, logo, favicon
- `heart_risk_prediction_regression_model.sav` — Pre-trained model (joblib)

## Deployment notes
- The app currently runs with Flask's development server (debug=True). For production, use a WSGI server (Gunicorn / uWSGI) behind a reverse proxy.
- Create environment variables or configuration for any sensitive settings and remove `debug=True` before production.


