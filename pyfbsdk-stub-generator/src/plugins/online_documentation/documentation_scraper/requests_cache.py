"""
This module handles caching of web pages useful while developing this module,
to avoid re-downloading the online documentation over and over again.
"""

import tempfile

from urllib.parse import quote
from pathlib import Path

import requests


CACHE_DIRNAME = "pyfbsdk_stub_generator_documentation_cache"


def get_cache_dir() -> Path:
    return Path(tempfile.gettempdir()) / CACHE_DIRNAME


def url_to_filepath(url: str) -> str:
    # Remove fragments from the url, to avoid caching the same page multiple times
    if "#" in url:
        url = url.partition("#")[0]

    return quote(url, safe="")


def get_cached_filepath(url: str) -> Path:
    return get_cache_dir() / url_to_filepath(url)


def get_request(url: str, timeout: int = 10, use_cache: bool = False) -> str:
    """
    A get http get request that caches the response in a temp file.  
    If the same url has been requested/cached before, it will return the cached response instead of making a new request.

    Returns the HTML content of the page as a string.
    """

    cached_file = get_cached_filepath(url)
    if use_cache and cached_file.exists():
        return cached_file.read_text(encoding="utf-8")

    try:
        response = requests.get(url, timeout=timeout)
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}")
        raise e

    if use_cache:
        cached_file.parent.mkdir(parents=True, exist_ok=True)
        cached_file.write_text(response.text, encoding="utf-8")

    return response.text
