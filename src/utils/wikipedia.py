"""
Module for interacting with the Wikipedia API to fetch disease-related information.

This module provides a function `wiki_api` that interacts with the Wikipedia API to retrieve
information about diseases based on the page IDs stored in the dataset.
"""

import requests as reqs

_BASE_URL = 'https://en.wikipedia.org/w/api.php'
_DEFAULT_PARAMS = {'action': 'query', 'prop': 'extracts', 'format': 'json'}

def wiki_api(**params) -> reqs.Response | None:
    """
    Makes a request to the Wikipedia API with the provided parameters.

    predefine params = {action: 'query', prop: 'extracts', format: 'json'}
    
    :param params: Parameters to pass to the Wikipedia API.
    :return: Response object or None if the request fails.
    """
    request_params = _DEFAULT_PARAMS.copy()
    request_params.update(params)
    try:
        res = reqs.get(_BASE_URL, request_params, timeout=10)
        res.raise_for_status()
        return res
    except reqs.exceptions.RequestException as e:
        print(f"(wiki-api)[Error]: {e}")
    return None
