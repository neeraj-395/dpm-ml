# Disease Prediction Model
A Web-based Disease Prediction Model using Machine Learning.

## Directory Structure

```bash
dmp-ml
├── data
│   ├── testing.csv
│   └── training.csv
├── LICENSE
├── models
│   └── decision_tree_model.pkl
├── README.md
├── requirements.txt
├── setup.py
├── src
│   ├── __init__.py
│   ├── models
│   │   ├── decision_tree.py
│   │   └── random_forest.py
│   ├── utils
│   │   ├── converters.py
│   │   ├── __init__.py
│   │   └── preprocess.py
│   └── visuals
│       ├── data_brvisual.py
│       └── data_htvisual.py
└── tests
    ├── test_models.py
    └── test_preprocessing.py
