DOCUMENTATION_URL = "https://help.autodesk.com/cloudhelp/"

PYTHON_REF_2024 = "ENU/MotionBuilder-SDK/py_ref/"  # 2024 and below use this URL
PYTHON_REF_2025 = "ENU/MOBU-PYTHON-API-REF/"  # 2025 and above use this URL


class EPythonNamespaces:
    PYFBSDK = "pyfbsdk"
    PYFBSDK_ADDITIONS = "pyfbsdk__additions"


def GetPythonRefUrl(Version: int):
    if 2025 <= Version:
        return PYTHON_REF_2025

    return PYTHON_REF_2024


def GetPythonTableOfContentsUrl(Namespace: str, Version: int):
    return f"{DOCUMENTATION_URL}{Version}/{GetPythonRefUrl(Version)}namespace{Namespace}.js"


def GetPythonPageContentsUrl(RelativeUrl: str, Version: int):
    return f"{DOCUMENTATION_URL}{Version}/{GetPythonRefUrl(Version)}{RelativeUrl}"
