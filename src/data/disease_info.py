"""
Module providing disease information using disease_info dataset and Wikipedia API.
This module allows retrieval of disease-related information, including precautions, image links,
doctor info, and a short summary fetched from Wikipedia.
"""

import yaml
import pandas as pd
from src.utils.wikipedia import wiki_api

class DiseaseInfo():
    """A class to provide disease-related information based on a dataset and Wikipedia API."""
    def __init__(self) -> None:
        self.__dinfo = self.__load_dataset()

    def __load_dataset(self) -> pd.DataFrame | None:
        """Load the disease information dataset from the specified path."""
        try:
            with open('config.yaml', encoding='utf-8') as file:
                data_path = yaml.safe_load(file)['metadata']['disease_info']
            return pd.read_csv(data_path).set_index('disease_name')
        except (OSError, FileNotFoundError) as e:
            print('(dinfo_module)', e)
        except KeyError as e:
            print(f'(dinfo_module) Unknown config key: {e}')
        return None

    def __safe_lookup(self, row: str, col: str) -> str | None:
        """Helper method to safely lookup data in the dataset with exception handling."""
        try:
            return self.__dinfo.loc[row, col] # type: ignore
        except AttributeError:
            print(f"(dinfo-module)[Error -1]: looking up '{col}' for '{row}'")
            return None

    def precautions(self, disease_name) -> list[str] | None:
        """Return a list of precautions for the given disease, if available."""
        precautions_str = self.__safe_lookup(disease_name, 'precautions')
        return precautions_str.split(',') if precautions_str else None

    def image_link(self, disease_name) -> str | None:
        """Return the image link for the given disease, if available."""
        return self.__safe_lookup(disease_name, 'wiki_img')

    def doctor_info(self, disease_name) -> dict[str, str | None]:
        """Return a dictionary with doctor info (name, branch, hospital) for the given disease."""
        keys = ['doctor_name', 'hospital', 'specialty']
        return dict(zip(keys, [self.__safe_lookup(disease_name, x) for x in keys]))

    def short_summary(self, disease_name: str) -> str | None:
        """Return a short summary of the disease from Wikipedia for the given disease."""
        pageid = self.__safe_lookup(disease_name, 'wiki_pageid')
        if pageid is None:
            return None
        try:
            res = wiki_api(pageids=pageid, exintro=True, explaintext=True, exsentences=5)
            if res and res.ok:
                return res.json()['query']['pages'][f'{pageid}']['extract'] # type:ignore
            return None
        except (KeyError, TypeError) as e:
            print('(dinfo-module)[Error -1]: Unable to locate', e)
            return None

if __name__ == "__main__":
    di = DiseaseInfo()
    print(di.short_summary('Fungal infection'))
    print(di.doctor_info('Fungal infection'))
    print(di.precautions('Fungal infection'))
    print(di.image_link('Fungal infection'))
