""" 
This module is responsible for scraping the table of contents from the online documentation
"""
from __future__ import annotations

import ast

from . import requests_cache

def get_base_url(version: int) -> str:
    return f"https://help.autodesk.com/cloudhelp/{version}/ENU/MOBU-PYTHON-API-REF/"

def get_full_url(version: int, relative_url: str):
    return f"{get_base_url(version)}{relative_url}"


def get_table_of_contents_python(module_name: str, version: int, use_cache: bool = False) -> dict[str, str]:
    """
    Get the table of contents for the given namespace and version

    Returns a dict mapping the name of the item to its url
    """
    url = get_full_url(version, f"namespace{module_name}.js")
    code, text = requests_cache.get_request(url, use_cache=use_cache)
    
    if "<title>404 Not Found</title>" in text:
        return {}

    # response should look like this:
    # var namespacepyfbsdk =\n[\n ["Enumeration", "classpyfbsdk_1_1_enumeration.html", null], ...];

    parsable_str = text.partition("=")[2]
    parsable_str = parsable_str.strip(" ;\n")
    parsable_str = parsable_str.replace("null", "None") # TODO: This may replace null in strings, use regex instead 

    parsed_response = ast.literal_eval(parsable_str)

    # Validate the parsed response
    if not all(len(item) == 3 for item in parsed_response):
        raise ValueError("Parsed response is not in the expected format")

    return {item[0]: get_full_url(version, item[1]) for item in parsed_response}
