"""
Disease Prediction Web Application

This Flask-based web application allows users to input symptoms and receive a predicted disease. 
"""
import base64
from flask import Flask, request, render_template
from src.data.disease_info import DiseaseInfo
from src.models.dp_model import DiseasePredictModel

import src.visuals.piechart as pie

app = Flask(__name__)

di = DiseaseInfo()
dpm = DiseasePredictModel()

@app.route("/")
def index_page():
    """Renders the homepage with a list of symptoms."""
    if dpm.symptoms is None:
        return render_template('500.html'), 500
    return render_template('index.html', symp_names=dpm.symptoms)

@app.route("/predict", methods=['GET'])
def predict():
    """Handles disease prediction based on user symptoms."""
    user_symp = request.args.get('symptoms', 'unknown').split(',')
    pred_probs = dpm.predict_proba(user_symp)

    if pred_probs is None or dpm.diseases is None:
        return render_template('500.html'), 500

    labels, probs = pie.filter_proba(dpm.diseases, pred_probs, 0.05)
    pred_disease = labels[max(range(len(probs)), key=lambda i: probs[i])]

    pie_image = pie.disease_piechart(labels, probs)

    return render_template(
        'result.html',
        d_name = pred_disease,
        d_summary = di.short_summary(pred_disease),
        d_image_url = di.image_link(pred_disease),
        d_precautions = di.precautions(pred_disease),
        d_doctor_info = di.doctor_info(pred_disease),
        piechart_data = base64.b64encode(pie_image.read()).decode()
    )

if __name__ == "__main__":
    app.run(debug=True)
