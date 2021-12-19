# Script for parsing the MB documentation and creating a json table with all of the avaliable pages

import json
import os
import re

from urllib import request

# https://download.autodesk.com/us/motionbuilder/sdk-documentation/
# https://download.autodesk.com/us/motionbuilder/sdk-documentation/contents-data.html

DOCS_URL = "https://download.autodesk.com/us/motionbuilder/sdk-documentation/"
TABLE_OF_CONTENT_URL = "%sscripts/toc-treedata.js" % DOCS_URL

DOCUMENTATION_DIR = os.path.join(
    os.path.dirname(__file__), "..", "documentation")


class FDictTags:
    Title = "ttl"
    Url = "ln"
    Id = "id"
    Children = "children"
    Ic = "ic"

    def Values(self):
        Values = [getattr(self, x) for x in dir(self) if not x.startswith("_")]
        return [x for x in Values if isinstance(x, str)]


class EPageType:
    Unspecified = -1
    Guide = 0
    C = 1
    Python = 2
    Examples = 3


# ------------------------------------------
#           Helper Functions
# ------------------------------------------

def GetUrlContent(Url: str):
    Response = request.urlopen(Url)
    return Response.read().decode('utf-8')


# ------------------------------------------
#             Documentation Page
# ------------------------------------------

class MoBuDocumentationPage():
    def __init__(self, PageInfo):
        self._PageInfo = PageInfo
        self.Title = PageInfo.get(FDictTags.Title)
        self.Id = PageInfo.get(FDictTags.Id)
        self.RelativeURL = PageInfo.get(FDictTags.Url)

    def __repr__(self):
        return '<object %s, "%s">' % (type(self).__name__, self.Title)

    def GetURL(self, bIncludeSideBar = False):
        if bIncludeSideBar:
            return DOCS_URL + "?url=%s,topicNumber=%s" % (self.RelativeURL, self.Id)
        return DOCS_URL + self.RelativeURL

    def LoadPage(self):
        RawHTML = GetUrlContent(self.GetURL())


class MoBuDocumentationCategory(MoBuDocumentationPage):
    def __init__(self, PageInfo):
        super().__init__(PageInfo)
        self.Pages = []
        self.SubCategories = []
        self.LoadChildren(PageInfo)

    def LoadChildren(self, PageInfo):
        for ChildPage in PageInfo.get(FDictTags.Children, []):
            if FDictTags.Children in ChildPage:
                self.SubCategories.append(MoBuDocumentationCategory(ChildPage))
            else:
                self.Pages.append(MoBuDocumentationPage(ChildPage))

    def FindPage(self, PageName):
        for Page in self.Pages:
            if Page.Title == PageName:
                return Page
        for SubCategory in self.SubCategories:
            Page = SubCategory.FindPage(PageName)
            if Page:
                return Page


# ------------------------------------------
#             Table of Contents
# ------------------------------------------

class DocsTableOfContents():
    def __init__(self):
        self._Categories = []
        self.LoadData()

    def LoadData(self):
        RawContent = GetUrlContent(TABLE_OF_CONTENT_URL)
        for CategoryInfo in ParseTableOfContentString(RawContent):
            self._Categories.append(MoBuDocumentationCategory(CategoryInfo))

    def FindPage(self, PageName, PageType = EPageType.Unspecified):
        if PageType != EPageType.Unspecified:
            return self._Categories[PageType].FindPage(PageName)

        for ContentDict in self._Categories:
            Page = ContentDict.FindPage(PageName)
            if Page:
                return Page


def ParseTableOfContentString(TableOfContentString) -> list:
    """
    Parse the raw table of content .js file downloaded from the autodesk documentation webpage
    """
    JsonString = ""

    for Line in TableOfContentString.split(";"):
        if "%s:" % FDictTags.Title in Line:
            JsonString = Line
            break

    if not JsonString:
        return {}

    JsonString = JsonString.split("=")[1]

    for Key in FDictTags().Values():
        JsonString = JsonString.replace('%s:' % Key, '"%s":' % Key)

    return json.loads(JsonString)


# test = DocsTableOfContents().FindPage("FBApplication", EPageType.Python).LoadPage()
