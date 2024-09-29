"""
Module for Disease Dataset Preprocessing and Feature Extraction
"""

import pandas as pd

def data_preprocessor(csv_file_path: str) -> tuple[pd.DataFrame, pd.Series]:
    """
    Preprocess the disease dataset by loading it from a CSV file and 
    preparing the target variables for model training.
    """

    df = pd.read_csv(csv_file_path)

    if 'prognosis' not in df.columns:
        raise ValueError("'prognosis' column is required in the dataset.")

    # Convert the 'prognosis' column to categorical codes, extracting unique diseases
    df['prognosis'], _ = pd.factorize(df['prognosis'])

    symptoms = df.columns[:-1].tolist()

    return df[symptoms], df['prognosis']


