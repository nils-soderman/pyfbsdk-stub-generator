# Script for parsing the MB documentation and creating a json table with all of the avaliable pages

from typing import Dict

import json
import os
import re

from urllib import request

# https://download.autodesk.com/us/motionbuilder/sdk-documentation/
# https://download.autodesk.com/us/motionbuilder/sdk-documentation/contents-data.html

URL = "https://download.autodesk.com/us/motionbuilder/sdk-documentation/"
TABLE_OF_CONTENT_URL = "%sscripts/toc-treedata.js" % URL

DOCUMENTATION_DIR = os.path.join(
    os.path.dirname(__file__), "..", "documentation")

class FDictTags:
    Title = "ttl"
    Url = "ln"
    Id = "id"
    Children = "children"
    Ic = "ic"
    
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


def SaveData(Content, Filename):
    Filepath = os.path.join(DOCUMENTATION_DIR, "%s.json" % Filename)
    with open(Filepath, "w+") as File:
        json.dump(Content, File)

# ------------------------------------------
#             Documentation Page
# ------------------------------------------

class MoBuDocumentationPage():
    def __init__(self):
        pass
    
    def LoadPage(self):
        pass


# ------------------------------------------
#             Table of Contents
# ------------------------------------------

class DocsTableOfContents():
    def __init__(self):
        self._Content = [{}, {}, {}, {}]
        self.LoadData()
        
    def LoadData(self):
        RawContent = GetUrlContent(TABLE_OF_CONTENT_URL)
        self._Content = RawTableOfContentsToDicts(RawContent)
        
    def FindPage(self, PageName, PageType = EPageType.Unspecified):
        ContentToSearch = []
        if PageType == EPageType.Unspecified:
            ContentToSearch = self._Content
        else:
            ContentToSearch = [self._Content[PageType]]
        for ContentDict in ContentToSearch:
            pass

def RawTableOfContentsToDicts(TableOfContentString) -> list:
    JsonString = ""

    for Line in TableOfContentString.split(";"):
        if "%s:" % FDictTags.Title in Line:
            JsonString = Line
            break

    if not JsonString:
        return {}

    JsonString = JsonString.split("=")[1]

    for Key in ["id", "ttl", "ln", "ic", "children"]:
        JsonString = JsonString.replace('%s:' % Key, '"%s":' % Key)

    return json.loads(JsonString)


DocsTableOfContents()


a = [{'a': 1}, {'b': 2}]

print(zip(a))