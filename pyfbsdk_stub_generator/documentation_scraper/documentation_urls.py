DOCUMENTATION_URL = "https://help.autodesk.com/cloudhelp/"
PYTHON_REF = "ENU/MotionBuilder-SDK/py_ref/"


class EPythonNamespaces:
    PYFBSDK = "pyfbsdk"
    PYFBSDK_ADDITIONS = "pyfbsdk__additions"


def GetPythonTableOfContentsUrl(Namespace: str, Version: int):
    return f"{DOCUMENTATION_URL}{Version}/{PYTHON_REF}namespace{Namespace}.js"


def GetPythonPageContentsUrl(RelativeUrl: str, Version: int):
    return f"{DOCUMENTATION_URL}{Version}/{PYTHON_REF}{RelativeUrl}"
