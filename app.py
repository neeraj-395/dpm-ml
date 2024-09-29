from flask import Flask, render_template, request
from src.models.dp_model import DiseasePredictModel

app = Flask(__name__)

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
    return f"""
        <h1>User { user_name }, based on your symptoms { user_symp }</h1>
        <p>Your predicted condition is: <strong>{ pred_disease }</strong></p>
        <a href="/">Back to Home</a>
    """

if __name__ == "__main__":
    app.run(debug=True)
