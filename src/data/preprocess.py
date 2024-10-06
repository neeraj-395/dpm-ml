"""
Module for Disease Dataset Preprocessing and Feature Extraction
"""
import yaml
import pandas as pd

with open('config.yaml', encoding='utf-8') as file:
    config = yaml.safe_load(file)

test = pd.read_csv(config['rawdata']['testing'])
train = pd.read_csv(config['rawdata']['training'])

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

# Remove garbage columns
test = test.drop('fluid_overload.1', axis=1)
train = train.drop(train.columns[-1], axis=1)
train = train.drop('fluid_overload.1', axis=1)

train['prognosis'], diseases = pd.factorize(train['prognosis'])
test['prognosis'], _ = pd.factorize(test['prognosis'])

labels = pd.DataFrame({
    'symptom_name' : pd.Series(train.columns[:-1]),
    'disease_name' : pd.Series(diseases)
})

train.to_csv('data/processed/new_training.csv', index=False)
test.to_csv('data/processed/new_testing.csv', index=False)
labels.to_csv('data/meta/new_labels.csv', index=True, index_label='i')
