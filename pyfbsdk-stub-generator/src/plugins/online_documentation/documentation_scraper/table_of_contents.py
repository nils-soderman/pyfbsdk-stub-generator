""" 
This module is responsible for scraping the table of contents from the online documentation
"""
from __future__ import annotations

import ast

from . import requests_cache


DOCUMENTATION_URL = "help.autodesk.com/cloudhelp/"
PYTHON_API_REF = "ENU/MOBU-PYTHON-API-REF/"


def get_full_url(version: int, relative_url: str):
    return f"https://{DOCUMENTATION_URL}{version}/{PYTHON_API_REF}{relative_url}"


def get_table_of_contents_python(module_name: str, version: int, use_cache: bool = False) -> dict[str, str]:
    """
    Get the table of contents for the given namespace and version

    Returns a dict mapping the name of the item to its url
    """
    url = get_full_url(version, f"namespace{module_name}.js")
    response = requests_cache.get_request(url, use_cache=use_cache)

    # response should look like this:
    # var namespacepyfbsdk =\n[\n ["Enumeration", "classpyfbsdk_1_1_enumeration.html", null], ...];

    parsable_str = response.partition("=")[2]
    parsable_str = parsable_str.strip(" ;\n")
    parsable_str = parsable_str.replace("null", "None")

    parsed_response = ast.literal_eval(parsable_str)

    # Validate the parsed response
    if not all(len(item) == 3 for item in parsed_response):
        raise ValueError("Parsed response is not in the expected format")

    return {item[0]: get_full_url(version, item[1]) for item in parsed_response}
