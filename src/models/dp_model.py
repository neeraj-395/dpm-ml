"""
Module providing disease prediction functionality using pre-trained machine learning models.
This module can predict diseases based on user-provided symptoms.
"""

import yaml
import joblib
import pandas as pd
from scipy import stats

class DiseasePredictModel():
    """
    A class that encapsulates disease prediction functionality using trained models.
    """
    def __init__(self) -> None:
        self.__config = self.__load_config()
        self.__symptoms, self.__diseases = self.__load_labels()
        self.__dt_model, self.__rf_model = self.__load_models()

    def __load_config(self) -> dict:
        try:
            with open('config.yaml', 'r', encoding='utf-8') as file:
                return yaml.safe_load(file)
        except OSError as e:
            print("(dp_module)", e)
            return {}

    def __load_models(self):
        try:
            with open(self.__config['models']['dtm'], 'rb') as file:
                dt_model = joblib.load(file)
            with open(self.__config['models']['rfm'], 'rb') as file:
                rf_model = joblib.load(file)
            return dt_model, rf_model
        except OSError as e:
            print("(dp_module)", e)
        except KeyError as e:
            print(f"(dp_model) Unknown config key: {e}")
        return None, None

    def __load_labels(self) -> tuple[tuple[str], tuple[str]]:
        try:
            df = pd.read_csv(self.__config['metadata']['labels'])
            return tuple(df['symptom_name'].tolist()), tuple(df['disease_name'].tolist())
        except FileNotFoundError as e:
            print("(dp_module)", e)
        except KeyError as e:
            print(f"(dp_model) Unknown label key: {e}")
        return tuple(), tuple()

    def __validate_models(self) -> bool:
        """
        Validates if both models and data labels are loaded properly.
        Returns True if everything is loaded; otherwise, False.
        """
        if not self.__dt_model or not self.__rf_model:
            print("(dp_module) Models are not loaded properly.")
            return False
        if not self.__symptoms or not self.__diseases:
            print("(dp_module) Data labels are not loaded properly.")
            return False
        return True

    def __symptoms_to_df(self, psymptoms: list[str]) -> pd.DataFrame:
        """
        Converts a list of user-provided symptoms into a datafram based on the
        presence or absence of each symptom from the full list of symptoms.
        """
        binary_vector = [1 if symp in psymptoms else 0 for symp in self.__symptoms]
        return pd.DataFrame([binary_vector], columns=self.__symptoms)

    @property
    def symptoms(self) -> tuple[str]:
        """Symptom labels tuple read-only."""
        return self.__symptoms

    @property
    def diseases(self) -> tuple[str]:
        """Disease labels tuple read-only."""
        return self.__diseases

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
        return stats.mode([dt_pred, rf_pred], keepdims=False)[0][0]

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
    print(dpm.predict(['itching', 'skin_rash', 'chills']))
