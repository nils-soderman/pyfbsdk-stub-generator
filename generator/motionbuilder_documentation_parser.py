# Script for parsing the MB documentation and creating a json table with all of the avaliable pages

import tempfile
import shutil
import json
import os
import re

from urllib import request
from html.parser import HTMLParser

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

def GetCacheFolder():
    return os.path.join(tempfile.gettempdir(), "mobu-docs-cache")

def GetCacheFilepath(RelativeUrl):
    return os.path.join(GetCacheFolder(), *RelativeUrl.split("/"))

def ClearCache():
    shutil.rmtree(GetCacheFolder())
    
def ReadFile(Filepath):
    with open(Filepath, "r") as File:
        return File.read()

def SaveFile(Filepath, Content):
    # Make sure folder exists before writing the file
    if not os.path.isdir(os.path.dirname(Filepath)):
        os.makedirs(os.path.dirname(Filepath))
        
    with open(Filepath, "w+") as File:
        File.write(Content)

# ------------------------------------------
#               DocPage Parser
# ------------------------------------------
class FMoBuDocsParserItem():
    Item = "memitem"
    Name = "memname"
    Doc = "memdoc"
    ParameterNames = "paramname"
    ParameterTypes = "paramtype"
    
class FMoBoDocsParameterNames():
    NoDefaultValue = "NoDefaultValue"

class MoBuDocsHTMLParser(HTMLParser):
    def __init__(self, *, convert_charrefs: bool = ...):
        super().__init__(convert_charrefs=convert_charrefs)
        
        self.Items = []
        self.CurrentItem = None
        self.CurrentDataTag = None
        self.bCollectingDocData = False
        
    def handle_starttag(self, tag, attrs):
        Attributes = dict(attrs)
        if tag == "div":
            ClassName = Attributes.get("class")
            if ClassName == FMoBuDocsParserItem.Item:
                if self.CurrentItem:
                    self.Items.append(self.CurrentItem)
                self.CurrentItem = {}
            if ClassName == FMoBuDocsParserItem.Doc:
                self.CurrentDataTag = FMoBuDocsParserItem.Doc
        elif tag == "td" and not self.CurrentDataTag:
            self.CurrentDataTag = Attributes.get("class")

    def handle_endtag(self, tag):
        if self.CurrentDataTag == FMoBuDocsParserItem.Doc:
            if tag == "div":
                self.CurrentDataTag = None
        elif tag == "td":
            self.CurrentDataTag = None
        elif tag == "body" and self.CurrentItem:
            self.Items.append(self.CurrentItem)

    def handle_data(self, Data):
        #Data = Data.strip()
        if self.CurrentDataTag and self.CurrentItem != None and Data.strip():
            CurrentText = self.CurrentItem.get(self.CurrentDataTag, "")
            if CurrentText:
                CurrentText += " "
            if self.CurrentDataTag != FMoBuDocsParserItem.Doc:
                Data = Data.strip()
            self.CurrentItem[self.CurrentDataTag] = CurrentText + Data
            
    def GetMembers(self):
        return [MoBuDocMember(x) for x in self.Items]

class MoBuDocParameter():
    def __init__(self, Name, Type, Default = FMoBoDocsParameterNames.NoDefaultValue):
        self.Name = Name
        self.Type = Type
        self.Default = Default
        
        def __repr__(self):
            return '<object %s, %s:%s = %s>' % (type(self).__name__, self.Title, self.Type, self.Default)

class MoBuDocMember():
    def __init__(self, Data):
        self.Name = ""
        self.Type = None
        self.bDeprecated = False
        self.Params = []
        self.DocString = ""
        
        self.LoadData(Data)
        
    def LoadData(self, Data):
        # Name & Type
        self.Name = Data.get(FMoBuDocsParserItem.Name, "")
        self.bDeprecated = self.Name.startswith("K_DEPRECATED")
        if self.bDeprecated:
            self.Name = self.Name.replace("K_DEPRECATED", "").strip()
        if " " in self.Name:
            self.Type, self.Name = self.Name.split(" ")
        
        # Parameters
        ParameterTypes = Data.get(FMoBuDocsParserItem.ParameterTypes)
        ParameterNames = Data.get(FMoBuDocsParserItem.ParameterNames)
        if ParameterTypes and ParameterNames:
            ParameterTypes = ParameterTypes.split(" ")
            ParameterNames = ParameterNames.split(",")
            if len(ParameterNames) != len(ParameterTypes):
                raise Exception("Lenght of ParamTypes & ParamNames does not match!")
            for Type, Name in zip(ParameterTypes, ParameterNames):
                DefaultValue = FMoBoDocsParameterNames.NoDefaultValue
                if "=" in Name:
                    Name, DefaultValue = (x.strip() for x in Name.split("="))
                self.Params.append(MoBuDocParameter(Name, Type, DefaultValue))
        
        # Doc String
        self.DocString = Data.get(FMoBuDocsParserItem.Doc)
        
        
# ------------------------------------------
#             Documentation Page
# ------------------------------------------

class MoBuDocumentationPage():
    def __init__(self, PageInfo, bLoadPage = False):
        self._PageInfo = PageInfo
        self.Title = PageInfo.get(FDictTags.Title)
        self.Id = PageInfo.get(FDictTags.Id)
        self.RelativeURL = PageInfo.get(FDictTags.Url)
        self.Members = []
        if bLoadPage:
            self.LoadPage()

    def __repr__(self):
        return '<object %s, "%s">' % (type(self).__name__, self.Title)

    def GetURL(self, bIncludeSideBar = False):
        if bIncludeSideBar:
            return DOCS_URL + "?url=%s,topicNumber=%s" % (self.RelativeURL, self.Id)
        return DOCS_URL + self.RelativeURL

    def LoadPage(self, bCache = False):
        CacheFilepath = GetCacheFilepath(self.RelativeURL)
        RawHTML = ""
        if bCache and os.path.isfile(CacheFilepath):
            RawHTML = ReadFile(CacheFilepath)
        else:
            RawHTML = GetUrlContent(self.GetURL())
            if bCache:
                SaveFile(CacheFilepath, RawHTML)
        Parser = MoBuDocsHTMLParser()
        Parser.feed(RawHTML)
        self.Members = Parser.GetMembers()
        
    def FindMember(self, Name):
        for Member in self.Members:
            if Member.Name == Name:
                return Member


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

    def FindPage(self, PageName, bLoadPage = False, bCache = False):
        for Page in self.Pages:
            if Page.Title == PageName:
                return Page
        for SubCategory in self.SubCategories:
            Page = SubCategory.FindPage(PageName, bLoadPage)
            if Page:
                if bLoadPage:
                    Page.LoadPage(bCache)
                return Page


# ------------------------------------------
#             Table of Contents
# ------------------------------------------

class DocsTableOfContents():
    def __init__(self, bCache = False):
        self._Categories = []
        self.LoadData()
        self.bCache = bCache

    def LoadData(self):
        RawContent = GetUrlContent(TABLE_OF_CONTENT_URL)
        for CategoryInfo in ParseTableOfContentString(RawContent):
            self._Categories.append(MoBuDocumentationCategory(CategoryInfo))

    def FindPage(self, PageName, PageType = EPageType.Unspecified, bLoadPage = True) -> MoBuDocumentationPage:
        if PageType != EPageType.Unspecified:
            return self._Categories[PageType].FindPage(PageName, bLoadPage, self.bCache)

        for ContentDict in self._Categories:
            Page = ContentDict.FindPage(PageName, bLoadPage, self.bCache)
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
