"""
Module providing disease prediction functionality using pre-trained machine learning models.
This module can predict diseases based on user-provided symptoms.
"""

import joblib
import pandas as pd
from scipy import stats

TEST_DATA_PATH = 'data/testing.csv'
DTM_PATH       = 'models/decision_tree_model.pkl'
RFM_PATH       = 'models/random_forest_model.pkl'

class DiseasePredictModel():
    """
    A class that encapsulates disease prediction functionality using trained models.
    """
    def __init__(self) -> None:
        self.__dt_model = None
        self.__rf_model = None
        self.__symptoms: list[str] = []
        self.__diseases: list[str] = []
        self.__load_models()
        self.__load_data_labels()

    def __load_models(self) -> None:
        try:
            with open(DTM_PATH, 'rb') as file:
                self.__dt_model = joblib.load(file)
            with open(RFM_PATH, 'rb') as file:
                self.__rf_model = joblib.load(file)
        except OSError as e:
            print("(dp_module)", e)

    def __load_data_labels(self) -> None:
        try:
            df = pd.read_csv(TEST_DATA_PATH)
            self.__symptoms.extend(df.columns[:-1].tolist())
            self.__diseases.extend(df['prognosis'].tolist())
        except FileNotFoundError as e:
            print("(dp_module)", e)

    def __validate_models(self) -> bool:
        """
        Validates if both models and data labels are loaded properly.
        Returns True if everything is loaded; otherwise, False.
        """
        if not self.__dt_model or not self.__rf_model:
            print("(dp_module) [Error -1]: Models are not loaded properly.")
            return False
        if not self.__symptoms or not self.__diseases:
            print("(dp_module) [Error -1]: Data labels are not loaded properly.")
            return False
        return True

    def __symptoms_to_df(self, psymptoms: list[str]) -> pd.DataFrame:
        """
        Converts a list of user-provided symptoms into a datafram based on the
        presence or absence of each symptom from the full list of symptoms.
        """
        binary_vector = [1 if symp in psymptoms else 0 for symp in self.__symptoms]
        return pd.DataFrame([binary_vector], columns=self.__symptoms)

    def get_symptoms(self) -> list[str]:
        """
        Return a list of symptom names
        """
        return self.__symptoms.copy()

    def get_diseases(self) -> list[str]:
        """
        Return a list of disease names
        """
        return self.__diseases.copy()

    def predict(self, symptoms_names: list[str]) -> int | None:
        """
        Predicts the disease based on the given symptoms using both
        decision tree and random forest models.
        """
        if not self.__validate_models():
            return None

        x_pred = self.__symptoms_to_df(symptoms_names)
        dt_pred = self.__dt_model.predict(x_pred) # type:ignore
        rf_pred = self.__rf_model.predict(x_pred) # type:ignore
        return stats.mode([dt_pred, rf_pred])[0][0]

    def predict_proba(self, symptoms_names: list[str]) -> list[float] | None:
        """
        Predicts the probability of each disease based on the given symptoms.
        """
        if not self.__validate_models():
            return None

        x_pred = self.__symptoms_to_df(symptoms_names)
        dt_proba = self.__dt_model.predict_proba(x_pred) # type:ignore
        rf_proba = self.__rf_model.predict_proba(x_pred) # type:ignore
        return ((dt_proba + rf_proba) / 2)[0]

if __name__ == "__main__":
    dpm = DiseasePredictModel()
    print(dpm.predict_proba(['itching', 'skin_rush', 'chills']))
