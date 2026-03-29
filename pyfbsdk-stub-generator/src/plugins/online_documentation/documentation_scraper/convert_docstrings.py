"""
Convert HTML descriptions into markdown docstrings
"""

from __future__ import annotations

import re
import string
import typing

import markdownify
from bs4 import Tag

from .utils import EClassName, get_parameter_nice_name


PY2_TO_PY3_PRINT_PATTERN = re.compile(r"(?<!\w)print\s+(.*)\s*(?<!\\)(?:\n|$)")


def get_safe_text(text: str) -> str:
    # Remove any non-breaking spaces and strip the text of whitespace and commas
    return text.replace('\xa0', ' ').strip(string.whitespace + ",").replace("\\", "\\\\")


class DocstringMarkdown(markdownify.MarkdownConverter):
    def __init__(self, page_url: str, param_nice_name = True, **options):
        super().__init__(**options)

        self.page_url = page_url
        self.param_nice_name = param_nice_name

    def description_to_markdown(self, html_description: str):
        docstring = self.convert(html_description)

        # There are some (what I guess is) broken <b> tags scattered around in the docstrings. Remove them.
        docstring = docstring.replace("b>", " ")

        # Replace single backslashes followed by special characters with the character only
        docstring = re.sub(r'(?<!\\)\\([*_])', r'\1', docstring)
        # Replace single backslashes followed by letters/numbers with double backslashes
        docstring = re.sub(r'(?<!\\)\\([a-zA-Z0-9\s])', r'\\\\\1', docstring)

        docstring = docstring.strip()

        # Go through and patch up the generated docstring
        parts = re.split(r'(```[\s\S]*?```)', docstring)
        for i, part in enumerate(parts):
            if i % 2 == 0:  # Outside code blocks
                part = re.sub(r'\n{3,}', '\n\n', part)                        # max 1 empty line
                part = re.sub(r'^[ \t]+(?!-)', '', part, flags=re.MULTILINE)  # strip indent except bullet points
                parts[i] = part
        docstring = "".join(parts)

        return docstring

    def convert_a(self, el: Tag, text, **options):
        """ Make sure all <a> tags have a full URL. """
        href = typing.cast(str | None, el.get("href"))
        if not href:
            return text
        
        if href.startswith("#"):
            href = f"{self.page_url}{href}"

        elif not href.startswith("http"):
            base = self.page_url.rpartition("/")[0]
            href = f"{base}/{href}"

        return f"[{text}]({href})" 

        # return super().convert_a(el, text, **options)  # type: ignore

    def convert_p(self, el, text, **options):
        return text.strip() + "\n\n"

    # -------------------------
    #      Parameter Lists
    # -------------------------

    def convert_dt(self, el: Tag, text, **options):
        """ Convert all <dt> tags to a headers. """
        # header_text = self.convert(str(el))
        inner_html = ''.join(str(child) for child in el.children)
        inner_text = self.convert(inner_html).strip()
        return f"### {inner_text}:\n"

    def convert_dd(self, el: Tag, text: str, **options):
        # Only strip new lines
        return text.strip("\n") + "\n"

    def convert_table(self, el: Tag, text, **options) -> str:
        # Check if element has the class name for a parameter list
        class_names = el.get("class")
        if class_names and EClassName.PARAMETER_TABLE in class_names:
            parameter_lines = []
            for tr_tag in el.find_all("tr"):
                line = ""

                for index, td_tag in enumerate(tr_tag.find_all("td")):
                    if index == 0 and EClassName.PARAMETER_NAME in td_tag.get("class", []):
                        parameter_name = get_safe_text(td_tag.get_text())
                        if self.param_nice_name:
                            parameter_name = get_parameter_nice_name(parameter_name)
                        line = f"    - {parameter_name}: "
                    else:
                        line += self.convert(str(td_tag)).strip(string.whitespace + "|")

                parameter_lines.append(line)

            return "\n".join(parameter_lines)

        return text  # super().convert_table(el, text, convert_as_inline)

    # -------------------------
    #      Code Blocks
    # -------------------------

    def convert_div(self, el: Tag, text, **options):
        """ Convert all <div> tags to a code block. """
        class_names = el.get("class")
        if class_names and EClassName.CODE_BLOCK in class_names:
            return self.convert_pre(el, text, **options)

        return text

    def convert_pre(self, el: Tag, text, **options):
        # Exclude any <div> tags that have class names "ttc"
        for child in el.find_all('div', class_='ttc'):
            child.decompose()

        code = get_safe_text(el.get_text()).strip("`")
        language_type = determine_language_from_code(code)

        if language_type == "python":
            # Replace Python 2 print statements with Python 3 print functions
            code = re.sub(PY2_TO_PY3_PRINT_PATTERN, r"print(\1)\n", code).strip()

        return f"\n```{language_type}\n{code}\n```\n"


def determine_language_from_code(code: str) -> typing.Literal['python', 'c++']:
    """ 
    Determine if the given code snippet is more likely to be Python or C++.
    """
    score_python = 0
    score_cpp = 0

    for line in code.splitlines():
        if line.startswith("//"):
            score_cpp += 1
        elif line.startswith(("#", "def ", "import ", "elif ")):
            score_python += 1

        # Look for line endings
        stripped_line = line.strip()
        if stripped_line.endswith(":"):
            score_python += 1
        elif stripped_line.endswith(";"):
            score_cpp += 1

    return "python" if score_python >= score_cpp else "c++"
