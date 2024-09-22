"""
Module for Disease Dataset Preprocessing and Feature Extraction
"""

import os
import pandas as pd

def data_preprocessor(csv_file_path: str) -> tuple[pd.DataFrame, pd.Series]:
    """
    Preprocess the disease dataset by loading it from a CSV file and 
    preparing the target variables for model training.

    Parameters
    -----------
    csv_file : str
        The path to the CSV file containing the disease dataset.

    Returns
    --------
        X : pd.DataFrame
            A DataFrame containing the symptom columns, where each row represents 
            a patient's symptom set and each column corresponds to a specific symptom.
    
        y : pd.Series
            A pandas Series containing the encoded target variable ('prognosis'). 
            Each unique prognosis is converted to a categorical integer code.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist at the given path.
    
    ValueError
        If 'prognosis' feature not present in dataset.

    Example
    --------
    >>> X, y, diseases, symptoms = data_preprocessor('dataset.csv')
    >>> print(X.head())
    >>> print(y.head())
    >>> print(diseases)
    >>> print(symptoms)
    """

    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"File not found {csv_file_path}")

    df = pd.read_csv(csv_file_path)

    if 'prognosis' not in df.columns:
        raise ValueError("'prognosis' column is required in the dataset.")

    # Convert the 'prognosis' column to categorical codes, extracting unique diseases
    df['prognosis'], _ = pd.factorize(df['prognosis'])

    symptoms = df.columns[:-1].tolist()
    # diseases = diseases.tolist()

    return df[symptoms], df['prognosis']


def extract_features(csv_file_path: str, feature_names: list[str]) -> tuple[list[str], ...]:
    """
    Extract specific feature columns from a CSV file and return them as a tuple of lists.

    Parameters
    ----------
    csv_file_path : str
        The path to the CSV file.

    feature_names : list[str]
        A list of feature names to be extracted from the CSV file.

    Returns
    -------
    tuple[list[str], ...]
        A tuple of lists where each list contains the values from the respective feature column. 
        If a feature is not found, a list containing 'None' is returned for that feature.

    Raises
    ------
    FileNotFoundError
        If the CSV file does not exist at the given path.

    Example
    -------
    >>> extract_features('data.csv', ['name', 'age', 'gender'])
    (['Alice', 'Bob'], ['25', '30'], ['Female', 'Male'])
    """
    # Check if the file exists
    if not os.path.exists(csv_file_path):
        raise FileNotFoundError(f"File not found {csv_file_path}")

    # Load CSV data
    df = pd.read_csv(csv_file_path)

    # Extract the requested feature columns or return ['None'] if not present
    return tuple(df[ft].tolist() if ft in df.columns else ['None'] for ft in feature_names)
