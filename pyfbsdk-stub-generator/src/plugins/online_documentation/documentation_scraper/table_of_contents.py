""" 
Web Documentation scraper for the pyfbsdk SDK.
"""
from __future__ import annotations

import ast
import requests

from . import documentation_cache as cache
from . import documentation_urls as urls
from . import page_parser


NAMESPACE_MODULE_MAP = {
    "pyfbsdk": "pyfbsdk",
    "pyfbsdk_additions": "pyfbsdk__additions"
}


class TableOfContentItem:
    def __init__(self, Data: list, Version: int, bUseCache: bool = False):
        if len(Data) != 3:
            raise ValueError(f"Data must be a list of 3 items. Got {len(Data)} items instead: {Data}")

        self.Name = Data[0]
        self.RelativeUrl = Data[1]
        # self.UrlNiceName = Data[2]  # Tbh, I have no idea what this is for
        self.Version = Version
        self.bUseCache = bUseCache

    def __repr__(self):
        return f"{self.__class__.__name__}<{self.Name}>"

    def GetPageUrl(self):
        return urls.GetPythonPageContentsUrl(self.RelativeUrl, self.Version)

    def ParsePage(self):
        Url = self.GetPageUrl()

        # Strip the hash from the url, to avoid caching the same page multiple times
        if "#" in Url:
            Url = Url.partition("#")[0]

        if self.bUseCache:
            PageContent = cache.CachedGetRequest(Url)
        else:
            PageContent = requests.get(Url, timeout=10).text

        BaseURL = urls.GetPythonPageContentsUrl("", self.Version)

        return page_parser.ParsePage(self.Name, PageContent, BaseURL)


class Documentation():
    def __init__(self, Namespace: str, Version: int, bUseCache = False) -> None:
        self.Namespace = Namespace
        self.Version = Version
        self.TableOfContents = GetPythonTableOfContents(Namespace, Version, bUseCache)

    def GetParsedPage(self, Name: str):
        for Page in self.TableOfContents:
            if Page.Name == Name:
                return Page.ParsePage()

        return None


def GetPythonTableOfContents(Namespace: str, Version: int, bUseCache: bool = False) -> list[TableOfContentItem]:
    url = urls.GetPythonTableOfContentsUrl(Namespace, Version)
    if bUseCache:
        response = cache.CachedGetRequest(url)
    else:
        response = requests.get(url, timeout=10).text
    
    # response should look like this:
    # var namespacepyfbsdk =\n[\n ["Enumeration", "classpyfbsdk_1_1_enumeration.html", null], ...];

    parsable_str = response.partition("=")[2]
    parsable_str = parsable_str.strip(" ;\n")
    parsable_str = parsable_str.replace("null", "None")

    parsed_response = ast.literal_eval(parsable_str)

    return [TableOfContentItem(data, Version, bUseCache) for data in parsed_response]


def GetNameSpaceFromModule(module_name: str) -> str | None:
    return NAMESPACE_MODULE_MAP.get(module_name)
