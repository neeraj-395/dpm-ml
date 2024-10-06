"""
Module for Disease Dataset Preprocessing and Feature Extraction
"""
import yaml
import pandas as pd

with open('config.yaml') as file:
    config = yaml.safe_load(file)

train = pd.read_csv(config['rawdata']['training'])
test = pd.read_csv(config['rawdata']['testing'])
labels = pd.read_csv(config['metadata']['labels'])


# Fix Spelling and Spacing Mistakes
for df in [train, test]:
    df['prognosis'] = df['prognosis'].replace({
        'Peptic ulcer diseae': 'Peptic ulcer disease',
        'Diabetes ' : 'Diabetes',
        'Hypertension ' : 'Hypertension',
        'hepatitis A' : 'Hepatitis A',
        'Osteoarthristis' : 'Osteoarthritis',
        'Dimorphic hemmorhoids(piles)' : 'Dimorphic hemorrhoids(piles)',
        '(vertigo) Paroymsal  Positional Vertigo' : 'Vertigo (Paroxysmal Positional Vertigo)'
    })



