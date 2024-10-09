"""
Disease Prediction Web Application

This Flask-based web application allows users to input symptoms and receive a predicted disease. 
"""

from flask import Flask, render_template, request
from src.data.disease_info import DiseaseInfo
from src.models.dp_model import DiseasePredictModel

app = Flask(__name__)

di = DiseaseInfo()
dpm = DiseasePredictModel()

@app.route("/")
def index_page():
    """Renders the homepage with a list of symptoms."""
    return render_template('index.html', symp_names=dpm.symptoms)

@app.route("/predict", methods=['GET'])
def predict():
    """Handles disease prediction based on user symptoms."""
    user_symp = request.args.get('symptoms', 'unknown').split(',')
    pred_index = dpm.predict(user_symp)
    pred_disease = dpm.diseases[pred_index] if pred_index else dpm.diseases[0]

    return render_template(
        'result.html',
        d_name = pred_disease,
        d_summary = di.short_summary(pred_disease),
        d_image_link = di.image_link(pred_disease)
    )

if __name__ == "__main__":
    app.run(debug=True)
