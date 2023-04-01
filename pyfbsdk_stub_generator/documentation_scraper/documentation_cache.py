
import tempfile
import re
import os

import requests

CACHE_DIRNAME = "pyfbsdk_stub_generator_documentation_cache"


def GetCacheDir():
    return os.path.join(tempfile.gettempdir(), CACHE_DIRNAME)


def UrlToFilepath(Url: str):
    return re.sub(r"[^a-zA-Z0-9]", "_", Url)


def GetCachedFilepath(Url: str):
    return os.path.join(GetCacheDir(), UrlToFilepath(Url))


def IsUrlCached(Url: str):
    return os.path.exists(GetCachedFilepath(Url))


def CacheUrl(Url: str, Content: str):
    CacheDir = GetCacheDir()
    if not os.path.exists(CacheDir):
        os.makedirs(CacheDir)

    Filepath = GetCachedFilepath(Url)
    with open(Filepath, "w", encoding="utf-8") as File:
        File.write(Content)


def CachedGetRequest(Url: str):
    if IsUrlCached(Url):
        with open(GetCachedFilepath(Url), "r", encoding="utf-8") as File:
            return File.read()
    else:
        Response = requests.get(Url, timeout=10)
        CacheUrl(Url, Response.text)
        return Response.text


def ClearCache():
    CacheDir = GetCacheDir()
    if os.path.exists(CacheDir):
        for File in os.listdir(CacheDir):
            os.remove(os.path.join(CacheDir, File))
        os.rmdir(CacheDir)
