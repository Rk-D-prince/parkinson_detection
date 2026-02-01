import numpy as np
import pandas as pd
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

# --- LOAD MODELS ---
# Using the paths provided in your snippet. 
# Ensure these files exist at these locations before running.
SVC_MODEL_PATH = r'C:\Users\RAJA KANNAN\Music\PARKINSON\CODING\frontend\svc_park.pkl'
XGB_MODEL_PATH = r'C:\Users\RAJA KANNAN\Music\PARKINSON\CODING\frontend\xgb_park.pkl'

try:
    svc_model = pickle.load(open(SVC_MODEL_PATH, 'rb'))
    xgb_model = pickle.load(open(XGB_MODEL_PATH, 'rb'))
    print("Models loaded successfully.")
except FileNotFoundError:
    print("Error: Model files not found. Check your file paths.")

@app.route('/')
def home():
    """Renders the main page with the input form."""
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    """
    Collects input from the form, processes it, and 
    returns a prediction from the chosen model.
    """
    if request.method == 'POST':
        try:
            # 1. Capture the model choice from form (SVM or XGBoost)
            selected_model_type = request.form.get('model_type')

            # 2. Extract 22 biomedical features from the form
            # Order must match the 'x' DataFrame columns used during training
            feature_values = [
                float(request.form['fo']), float(request.form['fhi']), float(request.form['flo']),
                float(request.form['jitter_percent']), float(request.form['jitter_abs']), 
                float(request.form['rap']), float(request.form['ppq']), float(request.form['ddp']),
                float(request.form['shimmer']), float(request.form['shimmer_db']), 
                float(request.form['apq3']), float(request.form['apq5']), float(request.form['apq']), 
                float(request.form['dda']), float(request.form['nhr']), float(request.form['hnr']),
                float(request.form['rpde']), float(request.form['dfa']), float(request.form['spread1']), 
                float(request.form['spread2']), float(request.form['d2']), float(request.form['ppe'])
            ]

            # 3. Convert to numpy array and reshape for prediction
            final_features = np.array(feature_values).reshape(1, -1)

            # 4. Perform prediction based on user model selection
            if selected_model_type == 'XGBoost':
                prediction = xgb_model.predict(final_features)
                model_used = "XGBoost Classifier"
            else:
                prediction = svc_model.predict(final_features)
                model_used = "Support Vector Machine"

            # 5. Map prediction to result string
            # Based on your status code: 1 = affected, 0 = not affected
            output = "AFFECTED" if prediction[0] == 1 else "NOT AFFECTED"
            result_color = "red" if prediction[0] == 1 else "green"

            return render_template('index.html', 
                                   prediction_text=f'Diagnosis: {output}',
                                   model_info=f'Predicted using: {model_used}',
                                   text_color=result_color)

        except Exception as e:
            return render_template('index.html', 
                                   prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)