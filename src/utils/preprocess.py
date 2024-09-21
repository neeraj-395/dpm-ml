"""
Module for Disease Dataset Preprocessing and Feature Extraction
"""

import pandas as pd

def data_proprocessor(csv_file_path: str) -> tuple[pd.DataFrame, pd.Series, list[str], list[str]]:

    """
    Preprocess the disease dataset by loading it from a CSV file and 
    preparing the feature and target variables for model training.

    Parameters
    -----------
    csv_file : str
        The path to the CSV file containing the disease dataset. 
        The dataset is expected to have symptom columns and a 'prognosis' column.

    Returns
    --------
        X : pd.DataFrame
            A DataFrame containing the symptom columns, where each row represents 
            a patient's symptom set and each column corresponds to a specific symptom.
    
        y : pd.Series
            A pandas Series containing the encoded target variable ('prognosis'). 
            Each unique prognosis is converted to a categorical integer code.
    
        diseases : list[str]
            A list of unique disease names from the dataset.
    
        symptoms : list[str]
            A list of the symptom column names from the dataset.

    Example
    --------
    >>> X, y, diseases, symptoms = data_preprocessor('dataset.csv')
    >>> print(X.head())
    >>> print(y.head())
    >>> print(diseases)
    >>> print(symptoms)
    """

    df = pd.read_csv(csv_file_path)

    # Convert the 'prognosis' column to categorical codes, extracting unique diseases
    df['prognosis'], diseases = pd.factorize(df['prognosis'])

    symptoms = df.columns[:-1].tolist()
    diseases = diseases.tolist()

    return df[symptoms], df['prognosis'], diseases, symptoms
