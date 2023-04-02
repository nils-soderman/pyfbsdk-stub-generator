""" 
Web Documentation scraper for the pyfbsdk SDK.
"""

from importlib import reload

import requests
import js2py

from . import documentation_cache as cache
from . import documentation_urls as urls
from . import page_parser

reload(cache)
reload(page_parser)


class ENamespaces:
    PYFBSDK = "pyfbsdk"
    PYFBSDK_ADDITIONS = "pyfbsdk__additions"


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
        if self.bUseCache:
            PageContent = cache.CachedGetRequest(Url)
        else:
            PageContent = requests.get(Url, timeout=10).text

        return page_parser.ParsePage(self.Name, PageContent)


class Documentation():
    def __init__(self, Namespace: str, Version: int, bUseCache = False) -> None:
        self.Namespace = Namespace
        self.Version = Version
        self.TableOfContents = GetPythonTableOfContents(Namespace, Version, bUseCache)

    def GetParsedPage(self, Name: str):
        for Page in self.TableOfContents:
            if Page.Name == Name:
                return Page.ParsePage()

        raise ValueError(f"Page with name {Name} not found in {self.Namespace} {self.Version}")


def GetPythonTableOfContents(Namespace: str, Version: int, bUseCache: bool = False) -> list[TableOfContentItem]:
    Url = urls.GetPythonTableOfContentsUrl(Namespace, Version)
    if bUseCache:
        Response = cache.CachedGetRequest(Url)
    else:
        Response = requests.get(Url, timeout=10).text

    ParsedResponse = js2py.eval_js(Response)

    return [TableOfContentItem(Data, Version) for Data in ParsedResponse]
