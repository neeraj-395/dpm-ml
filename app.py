from wikipediaapi import Wikipedia
from flask import Flask, render_template, request
from src.models.dp_model import DiseasePredictModel

app = Flask(__name__)

wiki = Wikipedia('DPM_ML_PROJECT')
dpm = DiseasePredictModel()
symptoms = dpm.get_symptoms()
diseases = dpm.get_diseases()

@app.route("/")
def index_page():
    return render_template('index.html', symp_names=symptoms)

@app.route("/predict", methods=['POST'])
def predict():
    user_name = request.form.get('username', 'Unknown')
    user_symp = request.form.get('symptoms', 'Unknown')
    pred_index = dpm.predict([user_symp])
    pred_disease = diseases[pred_index] if pred_index is not None else 'Unknown'
    disease_page = wiki.page(pred_disease)

    return render_template(
        'result.html',
        username = user_name,
        disease_desc = disease_page.summary,
        disease_title = disease_page.title
    )

if __name__ == "__main__":
    app.run(debug=True)
