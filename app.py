"""
Disease Prediction Web Application

This Flask-based web application allows users to input symptoms and receive a predicted disease. 
"""

from flask import Flask, render_template, request
from src.utils.disease_info import DiseaseInfo
from src.models.dp_model import DiseasePredictModel

app = Flask(__name__)

di = DiseaseInfo()
dpm = DiseasePredictModel()
symptoms = dpm.get_symptoms()
diseases = dpm.get_diseases()

@app.route("/")
def index_page():
    """Renders the homepage with a list of symptoms."""
    return render_template('index.html', symp_names=symptoms)

@app.route("/predict", methods=['POST'])
def predict():
    """Handles disease prediction based on user symptoms."""
    user_symp = request.form.get('symptoms', 'Unknown').split(',')
    pred_index = dpm.predict(user_symp)
    pred_disease = diseases[pred_index] if pred_index else diseases[0]

    return render_template(
        'result.html',
        d_name = pred_disease,
        d_summary = di.short_summary(pred_disease),
        d_image_link = di.image_link(pred_disease)
    )

if __name__ == "__main__":
    app.run(debug=True)
