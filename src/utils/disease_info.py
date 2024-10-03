"""
Module providing disease information using disease_info dataset and Wikipedia API.
This module allows retrieval of disease-related information, including precautions, image links,
doctor info, and a short summary fetched from Wikipedia.
"""

from pandas import DataFrame, read_csv
from src.utils.wikipedia import wiki_api

class DiseaseInfo():
    """
    A class to provide disease-related information based on a dataset and Wikipedia API.
    """
    def __init__(self) -> None:
        self.__data_path = 'data/disease_info.csv'
        self.__dinfo = self.__load_dataset()

    def __load_dataset(self) -> DataFrame | None:
        """Load the disease information dataset from the specified path."""
        try:
            return read_csv(self.__data_path).set_index('disease')
        except FileNotFoundError as e:
            print('(dinfo-module)', e)
            return None

    def __safe_lookup(self, row: str, col: str) -> str | None:
        """
        Helper method to safely lookup data in the dataset with exception handling.
        """
        try:
            return self.__dinfo.loc[row, col] # type: ignore
        except (KeyError, AttributeError):
            print(f"(dinfo-module)[Error -1]: looking up '{col}' for '{row}'")
            return None

    def precautions(self, disease_name) -> list[str] | None:
        """
        Return a list of precautions for the given disease, if available.
        """
        precautions_str = self.__safe_lookup(disease_name, 'precautions')
        return precautions_str.split(',') if precautions_str else None

    def image_link(self, disease_name) -> str | None:
        """
        Return the image link for the given disease, if available.
        """
        return self.__safe_lookup(disease_name, 'image_link')

    def doctor_info(self, disease_name) -> dict[str, str] | None:
        """
        Return a dictionary with doctor info (name, branch, hospital) for the given disease.
        """
        info_str = self.__safe_lookup(disease_name, 'doctor_info')
        return dict(zip(['name', 'branch', 'hospital'], info_str.split(','))) if info_str else None

    def short_summary(self, disease_name: str) -> str | None:
        """
        Return a short summary of the disease from Wikipedia for the given disease.
        """
        pageid = self.__safe_lookup(disease_name, 'wiki_pageid')
        if pageid is not None:
            try:
                res = wiki_api(pageids=pageid, exintro=True, explaintext=True, exsentences=5)
                return res['query']['pages'][str(pageid)]['extract'] # type:ignore
            except KeyError as e:
                print('(dinfo-module)[Error -1]: Unable to locate', e)
                return None
        else: return None

if __name__ == "__main__":
    disease_info = DiseaseInfo()
    summary = disease_info.short_summary('Fungal infection')
    print(summary)
