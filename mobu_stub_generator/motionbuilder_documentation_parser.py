import tempfile
import shutil
import json
import os
import re

from html.parser import HTMLParser
from urllib import request


# ------------------------------------------
#               URLs & Paths
# ------------------------------------------

# Base URLs where the MoBu docs are stored
AUTODESK_DOMAIN = "https://help.autodesk.com/"
MOBU_DOCS_VIEW_URL = AUTODESK_DOMAIN + "view/MOBPRO/"  # Base url used to view content
MOBU_DOCS_COULDHELP_URL = AUTODESK_DOMAIN + "cloudhelp/"  # Server that hosts the SDK doc files

ENU_FOLDER = "ENU/"

# Path to the main table of contents
DOC_GUIDE_CONTENTS_PATH = "data/toctree.json"

# Python paths to relevant table of contents
PY_REF_PATH = "MotionBuilder-SDK/py_ref/"
PYFBSDK_PATH = PY_REF_PATH + "group__pyfbsdk.js"
PYFBSDK_ADDITIONS_PATH = PY_REF_PATH + "group__pyfbsdk__additions.js"
PYTHON_EXAMPLES_PATH = PY_REF_PATH + "examples.js"

# SDK paths to table of contents
SDK_CPP_PATH = "MotionBuilder-SDK/cpp_ref/"
SDK_CLASSES_PATH = SDK_CPP_PATH + "annotated_dup.js"
SDK_FILES_PATH = SDK_CPP_PATH + "files_dup.js"


# ------------------------------------------
#               Strucs & Enums
# ------------------------------------------

CToPythonVariableTranslation = {
    "FBVector4": "FBVector4d",
    "FBTVector": "FBVector3d",
    "double": "float",
    "FBString": "str",
    "string": "str",
    "char": "str",
    "float": "float",
    "int": "int",
    "bool": "bool",
    "void": "None",
    "true": "True",
    "false": "False",
    "NULL": "None",
    "kInt64": "int",
    "kLong": "int",
    "kULong": "int",
    "kLongLong": "float",
    "kReference": ""
}


class FMoBoDocsParameterNames():
    Undefined = "NoDefaultValue"


class FDictTags:
    Title = "ttl"
    Url = "ln"
    Id = "id"
    Children = "children"
    Ic = "ic"

    def Values(*args):
        Values = [getattr(FDictTags, x) for x in dir(FDictTags) if not x.startswith("_")]
        return [x for x in Values if isinstance(x, str)]


class FMoBuDocsParserItem():
    Item = "memitem"
    Name = "memname"
    Doc = "memdoc"
    ParameterNames = "paramname"
    ParameterTypes = "paramtype"

    def GetValues(*args):
        Values = [getattr(FMoBuDocsParserItem, x) for x in dir(FMoBuDocsParserItem) if not x.startswith("_")]
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

def ConvertVariableTypeToPython(Type: str):
    """
    Convert a C++ variable type to a python variable
    Example: 'double' -> 'float'
    """
    # Remove type defenitions that doesn't carry any meaning when converted to python
    for Char in ["(void *)", "*", "&"]:
        if Char in Type:
            Type = Type.replace(Char, "").strip()

    # Arrays, in the pyfbsdk there are two FBVector4<dobule> arrays. convert these into FBVector4
    if "<" in Type:
        if not Type.startswith("FBVector"):
            return "List[%s]" % Type.partition("<")[2].partition(">")[0].strip()
        Type = Type.partition("<")[0].strip()

    if " " in Type:
        Type = Type.rpartition(" ")[2]

    # Check if variable needs to be translated into python, e.g. double -> float
    for Key, Value in CToPythonVariableTranslation.items():
        if Type.lower() == Key.lower():
            return Value

    # Remove f suffix from floats e.g. 0.0f -> 0.0
    if Type.endswith("f") and Type.replace(".", "").replace("f", "").isnumeric():
        return Type[:-1]

    Type = Type.replace("::", ".")

    return Type


def GetClosestSupportedMotionBuilderVersion(Version: int):
    """
    Get the closest MotionBuilder version that is supported 
    """
    if Version < 2018:
        return 2018

    if Version == 2021:
        return 2022

    return Version


def GetFullURL(Version, Path, bGetSource = False):
    BaseURL = MOBU_DOCS_COULDHELP_URL if bGetSource else MOBU_DOCS_VIEW_URL
    return "%s%s/%s%s" % (BaseURL, Version, ENU_FOLDER, Path)


def GetUrlContent(Url: str):
    print("Url: %s" %(Url))
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

    with open(Filepath, "w+", encoding="utf-8") as File:
        File.write(Content)


# ------------------------------------------
#           DocPage HTML Parser
# ------------------------------------------

class MotionBuilderDocumentationHtmlPageParser(HTMLParser):
    """
    HTML parser to fetch interesting content from a MotionBuilder SDK documentation page
    """

    def __init__(self, *, convert_charrefs: bool = ...):
        super().__init__(convert_charrefs=convert_charrefs)

        self.TotalItems = []  # Main list containin all found members as dicts

        self.CurrentItem = None  # Current item name
        self.CurrentItemDataTag = None  # Tag that the parser is collecting data for
        self.CurrentItemDataCollector = ""  # Data collected by the parser for the active tag

    def handle_starttag(self, tag, attrs):
        Attributes = dict(attrs)
        ClassName = Attributes.get("class")

        if tag == "div":
            if ClassName == FMoBuDocsParserItem.Item:
                if self.CurrentItem:
                    self.TotalItems.append(self.CurrentItem)
                self.CurrentItem = {}

            if ClassName == FMoBuDocsParserItem.Doc:
                self.CurrentItemDataTag = FMoBuDocsParserItem.Doc
                self.CurrentItemDataCollector = ""

        elif tag == "td" and not self.CurrentItemDataTag:
            if ClassName in FMoBuDocsParserItem.GetValues():
                self.CurrentItemDataTag = ClassName
                self.CurrentItemDataCollector = ""

    def handle_data(self, Data):
        if self.CurrentItemDataTag and self.CurrentItem != None and Data.strip():
            self.CurrentItemDataCollector += Data

    def handle_endtag(self, tag):
        if self.CurrentItemDataTag == FMoBuDocsParserItem.Doc:
            if tag == "div":
                self.CurrentItem[self.CurrentItemDataTag] = self.CurrentItemDataCollector
                self.CurrentItemDataTag = None

        elif tag == "td":
            if self.CurrentItem != None and self.CurrentItemDataTag:
                self.CurrentItemDataCollector = self.CurrentItemDataCollector.strip()

                CurrentList = self.CurrentItem.get(self.CurrentItemDataTag, [])
                CurrentList.append(self.CurrentItemDataCollector)
                self.CurrentItemDataCollector = CurrentList

                self.CurrentItem[self.CurrentItemDataTag] = self.CurrentItemDataCollector

            self.CurrentItemDataTag = None

        elif tag == "body" and self.CurrentItem:
            self.TotalItems.append(self.CurrentItem)

    #
    #   Custom Functions
    #

    def _DictToMoBuDocMember(self, Item: dict):
        """
        Convert a parsed item result to a 'MoBuDocMember' instance.
        """
        # Get name & type
        Name = Item.get(FMoBuDocsParserItem.Name, [""])[0]  # There should really only be one name, so grab the first one
        Type = None
        if " " in Name:
            # If name is e.g. 'const bool MyBoolean', split into ('const bool', 'MyBoolean')
            Type, Delimiter, Name = Name.rpartition(" ")

        # Generate a list of DocMemberParameter instances, based on the ParamNames/Types collected when parsing
        Params = []
        ParameterNames = Item.get(FMoBuDocsParserItem.ParameterNames, [])
        ParameterTypes = Item.get(FMoBuDocsParserItem.ParameterTypes, [])
        if ParameterNames and ParameterTypes:
            # Make sure the lists have the same lenght, if not something must have gone wrong when parsing.
            # if not len(ParameterNames) == len(ParameterTypes):
            #     raise Exception("%s has different array sizes in ParamNames & Types:\n%s\n%s" % (Name, str(ParameterNames), str(ParameterTypes)))

            for ParamName, ParamType in zip(ParameterNames, ParameterTypes):
                # If parameter has a default value, it'll be stored with the ParamName, example: 'MyParam = false'
                DefaultValue = FMoBoDocsParameterNames.Undefined
                if "=" in ParamName:
                    ParamName, DefaultValue = ParamName.split("=")
                    DefaultValue = DefaultValue.strip()
                    if DefaultValue.endswith(","):
                        DefaultValue = DefaultValue[:-1]
                    ParamName = ParamName.strip()

                # Make sure name doesn't end with a comma
                if ParamName.endswith(","):
                    ParamName = ParamName[:-1]

                if not ParameterTypes:
                    ParameterTypes = FMoBoDocsParameterNames.Undefined

                Params.append(DocMemberParameter(ParamName, ParamType, DefaultValue))

        # Get docstring, there should always just be one, so get the first one
        DocString = Item.get(FMoBuDocsParserItem.Doc, "")

        return DocPageMember(Name, Type, Params, DocString)

    def GetMembers(self):
        return [self._DictToMoBuDocMember(x) for x in self.TotalItems]


# ------------------------------------------
#             Main Classes
# ------------------------------------------

class DocMemberParameter():
    def __init__(self, Name, Type, Default = FMoBoDocsParameterNames.Undefined):
        self.Name = Name
        self.Type = Type
        self.Default = Default

    def GetType(self, bConvertToPython = False):
        if bConvertToPython:
            return ConvertVariableTypeToPython(self.Type)
        return self.Type

    def GetDefaultValue(self, bConvertToPython = False):
        if self.Default == FMoBoDocsParameterNames.Undefined:
            return FMoBoDocsParameterNames.Undefined

        if bConvertToPython:
            return ConvertVariableTypeToPython(self.Default)

        return self.Default

    def __repr__(self):
        return '<object %s: %s:%s = %s>' % (type(self).__name__, self.Name, self.Type, self.Default)


class DocPageMember():
    def __init__(self, Name, Type = None, Params = [], DocString = ""):
        self.Name = Name
        self.Type = Type
        self.Params = Params
        self.DocString = DocString

    def GetType(self, bConvertToPython = False):
        if bConvertToPython:
            return ConvertVariableTypeToPython(self.Type)
        return self.Type

    def __repr__(self):
        return '<object DocPageMember: %s>' % (self.Name)


class DocumentationPage():
    def __init__(self, Version, Title, RelativeURL, Id = None, bLoadPage = False):
        self.Version = Version
        self.Title = Title
        self.RelativeURL = RelativeURL
        self.Id = Id
        self.bIsLoaded = False
        self.Members = {}
        if bLoadPage:
            self.LoadPage()

    def __repr__(self):
        return '<object %s, "%s">' % (type(self).__name__, self.Title)

    def GetURL(self):
        return GetFullURL(self.Version, self.RelativeURL, bGetSource = True)

    def GetURLRelativeToENU(self):
        if self.RelativeURL and ENU_FOLDER in self.RelativeURL:
            return self.RelativeURL.partition(ENU_FOLDER)[2]
        return self.RelativeURL

    def LoadPage(self, bCache = False):
        if self.bIsLoaded:
            return
        CacheFilepath = GetCacheFilepath(self.RelativeURL)
        if "#" in CacheFilepath:
            CacheFilepath = CacheFilepath.partition("#")[0]
        RawHTML = ""
        if bCache and os.path.isfile(CacheFilepath):
            RawHTML = ReadFile(CacheFilepath)
        else:
            RawHTML = GetUrlContent(self.GetURL())
            if bCache:
                SaveFile(CacheFilepath, RawHTML)
        Parser = MotionBuilderDocumentationHtmlPageParser()
        Parser.feed(RawHTML)

        self.Members = {x.Name: x for x in Parser.GetMembers()}

    def GetMember(self, Name):
        return self.Members.get(Name, None)


class DocumentationCategory(DocumentationPage):
    def __init__(self, Version, ParsedData, bLoadPage = False):
        super().__init__(Version,
                         Title = ParsedData.get(FDictTags.Title),
                         RelativeURL = ParsedData.get(FDictTags.Url),
                         Id = ParsedData.get(FDictTags.Id),
                         bLoadPage = bLoadPage)
        self.Pages = []
        self.SubCategories = []

        self.LoadChildren(ParsedData)

    def LoadChildren(self, PageInfo):
        for ChildPage in PageInfo.get(FDictTags.Children, []):
            if FDictTags.Children in ChildPage:
                self.SubCategories.append(DocumentationCategory(self.Version, ChildPage))
            else:
                self.Pages.append(DocumentationPage(self.Version,
                                                    ChildPage.get(FDictTags.Title),
                                                    ChildPage.get(FDictTags.Url),
                                                    ChildPage.get(FDictTags.Id)))

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


class MotionBuilderDocumentation():
    def __init__(self, Version, bCache = False):
        self.Version = Version
        self.bCache = bCache
        self._TableOfContents = []
        self._SDKClasses = {}
        self._PythonExamples = {}
        self._PythonSDKToc = {}
        self._SDKContent = {}

    def GetSDKClasses(self):
        if self._SDKClasses:
            return self._SDKClasses
        ClassesContent = GetDocsSDKContent(self.Version, SDK_CLASSES_PATH, self.bCache)
        self._SDKClasses = {x[0]: DocumentationPage(self.Version, x[0], SDK_CPP_PATH + x[1]) for x in ClassesContent}
        return self._SDKClasses

    def GetSDKTableOfContents(self):
        if not self._SDKContent:
            Content = []
            for FileName, PageUrl, Id in GetDocsSDKContent(self.Version, SDK_FILES_PATH, self.bCache):
                if Id:
                    Content += GetDocsSDKContent(self.Version, "%s%s.js" % (SDK_CPP_PATH, Id), self.bCache)
            # TODO: Clean up
            self._SDKContent = self.GetSDKClasses()
            self._SDKContent.update({x[0]: DocumentationPage(self.Version, x[0], SDK_CPP_PATH + x[1]) for x in Content})
        return self._SDKContent

    def GetSDKClassPagesByName(self, ClassName, bLoadPage = True):
        Page = self.GetSDKTableOfContents().get(ClassName)
        if Page and bLoadPage:
            Page.LoadPage(self.bCache)
        return Page

    def GetSDKFunctionByName(self, FunctionName):
        Page = self.GetSDKTableOfContents().get(FunctionName)
        if Page:
            Page.LoadPage(self.bCache)
            return Page.GetMember(FunctionName)

    def GetMainTableOfContents(self):
        if not self._TableOfContents:
            self._TableOfContents = [DocumentationCategory(self.Version, x) for x in GetDocsMainTableOfContent(self.Version)]
        return self._TableOfContents

    def GetPythonSDKTableOfContents(self):
        if not self._PythonSDKToc:
            PyfbsdkContent = GetDocsSDKContent(self.Version, PYFBSDK_PATH, self.bCache)
            PyfbsdkAdditionsContent = GetDocsSDKContent(self.Version, PYFBSDK_ADDITIONS_PATH, self.bCache)
            AllPythonSDKContent = PyfbsdkContent + PyfbsdkAdditionsContent
            self._PythonSDKToc = {x[0]: DocumentationPage(self.Version, x[0], PY_REF_PATH + x[1]) for x in AllPythonSDKContent}
        return self._PythonSDKToc

    def FindPage(self, PageName, PageType = EPageType.Unspecified, bLoadPage = True) -> DocumentationPage:
        if PageType != EPageType.Unspecified:
            return self._TableOfContents[PageType].FindPage(PageName, bLoadPage, self.bCache)

        for ContentDict in self._TableOfContents:
            Page = ContentDict.FindPage(PageName, bLoadPage, self.bCache)
            if Page:
                return Page

    def GetPythonExamples(self):
        if not self._PythonExamples:
            PythonExamples = GetDocsSDKContent(self.Version, PYTHON_EXAMPLES_PATH)
            self._PythonExamples = {x[0]: DocumentationPage(self.Version, x[0], PY_REF_PATH + x[1]) for x in PythonExamples}
        return self._PythonExamples


# -------------------------------------------------------------
#             Functions for parsing table of contents
# -------------------------------------------------------------

def GetDocsSDKContent(Version, Path, bCache = False):
    """
    Get SDK table of contents
    """
    Content = None
    CacheFilepath = GetCacheFilepath(Path)
    bCacheFileExists = os.path.isfile(CacheFilepath)

    if bCache and bCacheFileExists:
        Content = ReadFile(CacheFilepath)
    else:
        Content = GetUrlContent(GetFullURL(Version, Path, bGetSource = True))

    if bCache and not bCacheFileExists:
        SaveFile(CacheFilepath, Content)

    return ParseSDKTableOfContent(Content)


def ParseSDKTableOfContent(RawJavascriptString):
    """
    Parse SDK table of content. This will be stored as a .js file, with all of the content saved in a single nested list variable
    * Example: 'var abc = ["PageTitle", "PageUrl", "PageID", ["ChildPageTitle", "PageUrl", "PageID", null]]'
    """
    # Make the javascript array readable in python
    Text = RawJavascriptString.replace(", null ]", ",None]")  # Replace null with None
    Text = Text.split("=", 1)[1]  # Remove variable defenition
    Text = Text.strip()

    # Remove trailing ;
    if Text.endswith(";"):
        Text = Text[:-1]

    # Evaluate the string to convert it into a python list
    return eval(Text)


def GetDocsMainTableOfContent(Version) -> list:
    """
    Get the MoBu Docs main TableOfContent.
    This is the 'help' section of the documentation. This is NOT the sdk documentation.
    """
    RawContent = GetUrlContent(GetFullURL(Version, DOC_GUIDE_CONTENTS_PATH))
    TableOfContent = json.loads(RawContent)
    return TableOfContent.get("books", {})

print(MotionBuilderDocumentation(2022, True).GetSDKFunctionByName("FBShowToolByName").GetType(bConvertToPython = True))