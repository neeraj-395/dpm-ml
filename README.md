# Disease Prediction Model

This project uses machine learning models (Decision Tree and Random Forest) to predict diseases based on symptoms. The web application is built using Flask, and users can input their symptoms to get predictions, along with relevant visualizations and information about the predicted disease.

## Prerequisites

- **Python**: Ensure you have the latest version installed. [Download Python](https://www.python.org/downloads/)
- **Make**: A project management tool for running tasks. [Download Make](https://www.gnu.org/software/make/)

## Installation

1. **Clone the repository**  
   Open your terminal and clone the repository using the following command:
   ```bash
   git clone https://github.com/neeraj-395/dpm-ml.git
   ```

2. **Create a virtual environment**  
   Navigate to the project root directory and create a virtual environment using `make`:
   ```bash
   cd disease-prediction
   make venv
   ```
   Alternatively, you can create a virtual environment manually:
   ```bash
   python -m venv <directory name>
   ```

3. **Install dependencies**  
   Run the following command to install the necessary packages:
   ```bash
   make build
   ```

4. **Start the application**  
   Use the following command to start the Flask application:
   ```bash
   make serve
   ```

5. **Access the application**  
   Open your browser and navigate to `http://127.0.0.1:5000/` to access the web application.

## Project Demo

Once the application is running, you can enter symptoms on the homepage and receive a prediction for the most likely disease. The result page will show:

https://github.com/user-attachments/assets/f77628b8-ae58-4661-ba9d-7dd31b711e89

## Project Directory Structure

```
.
├── app.py
├── config.yaml
├── data
│   ├── meta
│   │   ├── disease_info.csv
│   │   └── labels.csv
│   ├── processed
│   │   ├── testing.csv
│   │   └── training.csv
│   └── raw
│       ├── testing.csv
│       └── training.csv
├── LICENSE
├── Makefile
├── models
│   ├── decision_tree_model.pkl
│   └── random_forest_model.pkl
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── data
│   │   ├── disease_info.py
│   │   └── preprocess.py
│   ├── __init__.py
│   ├── models
│   │   ├── dp_model.py
│   │   └── train_models.py
│   ├── tests
│   │   ├── test_disease_info.py
│   │   ├── test_dp_model.py
│   │   ├── test_models.py
│   │   └── test_preprocessing.py
│   ├── utils
│   │   └── wikipedia.py
│   └── visuals
│       ├── barplot.py
│       ├── heatmap.py
│       └── piechart.py
├── static
│   ├── css
│   │   ├── 500.css
│   │   ├── common.css
│   │   ├── index.css
│   │   └── result.css
│   ├── img
│   │   ├── medical-robot.ico
│   │   └── medical-robot.png
│   └── js
│       └── index.js
└── templates
    ├── 500.html
    ├── index.html
    └── result.html

17 directories, 38 files
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
