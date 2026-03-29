import enum
import keyword


class EClassName(enum.StrEnum):
    MEMBER = "memitem"
    MEMBER_TITLE = "memtitle"
    MEMBER_DOC = "memdoc"
    MEMBER_NAME = "memname"
    CODE_BLOCK = "fragment"
    PAGE_DETAILED_DESC = "textblock"
    PARAMETER_NAME = "paramname"
    PARAMETER_TYPE = "paramtype"
    PARAMETER_TABLE = "params"


def get_parameter_nice_name(name: str) -> str:
    # Remove the "p" prefix from the parameter name, since arguments cannot be referenced as keywords
    if name.startswith("p") and not name[1].isnumeric():
        patched_name = name.lstrip("p")
        if patched_name not in keyword.kwlist:  # Make sure the patched variable name is not a keyword, e.g. 'True', 'None' etc.
            name = patched_name

    return name
