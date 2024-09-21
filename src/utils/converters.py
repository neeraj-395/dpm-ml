import numpy as np

def symptoms_to_vector(user_symptoms: list[str], all_symptoms: list[str]) -> np.ndarray:
    """
    Converts a list of user-provided symptoms into a binary feature vector based on the
    presence or absence of each symptom from the full list of symptoms.

    Args:
        user_symptoms (list[str]): A list of symptoms provided by the user.
        all_symptoms (list[str]): The complete list of all possible symptoms.

    Returns:
        np.ndarray: A binary vector where each element is:
            - 1 if the symptom is in `user_symps`.
            - 0 if the symptom is not in `user_symps`.

    Example:
    >>> all_symptoms = ['fever', 'cough', 'fatigue']
    >>> user_symptoms = ['fever', 'fatigue']
    >>> vector = symptoms_to_vector(user_symptoms, all_symptoms)
    >>> vector will be: array([1, 0, 1])
    """
    return np.array([1 if symptom in user_symptoms else 0 for symptom in all_symptoms])
