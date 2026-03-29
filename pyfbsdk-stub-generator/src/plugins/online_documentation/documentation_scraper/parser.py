"""
This module is responsible for parsing the HTML content of a pyfbsdk documentation page
"""

from __future__ import annotations

import string

from dataclasses import dataclass
from typing import cast

from bs4 import BeautifulSoup

from .convert_docstrings import DocstringMarkdown
from .utils import EClassName


@dataclass
class Parameter:
    name: str | None
    type_str: str | None
    default_value: str | None = None


@dataclass
class MemberItem:
    name: str
    type_str: str
    doc_string: str
    parameters: list[Parameter]
    relative_url: str


@dataclass
class ParsedPage:
    name: str
    description: str
    members: list[MemberItem]

    def find_member_by_name(self, member_name: str) -> MemberItem | None:
        for member in self.members:
            if member.name == member_name:
                return member
        return None
    
    def find_members_by_name(self, member_name: str) -> list[MemberItem]:
        return [member for member in self.members if member.name == member_name]


def get_safe_text(text: str) -> str:
    # Remove any non-breaking spaces and strip the text of whitespace and commas
    return text.replace('\xa0', ' ').strip(string.whitespace + ",").replace("\\", "\\\\")


def parse_page(page_name: str, page_html: str, page_url: str) -> ParsedPage:
    """
    Parse the HTML content of a page and return a DocumentationParsedPage object.

    ### Parameters:
        - `PageName`: The name of the page.
        - `PageHtmlContent`: The HTML content of the page.
        - `BaseURL`: The base URL to be used to resolve relative URLs.
    """
    docstring_markdown = DocstringMarkdown(page_url)

    parser = BeautifulSoup(page_html, "html.parser")

    page_description_html = parser.find("div", class_ = EClassName.PAGE_DETAILED_DESC)
    if page_description_html:
        page_description = docstring_markdown.description_to_markdown(str(page_description_html))
    else:
        page_description = ""

    members = parser.find_all("div", class_ = EClassName.MEMBER)
    member_titles = parser.find_all("h2", class_ = EClassName.MEMBER_TITLE)

    # If the titles doesn't match, fallback to not using titles
    if len(members) != len(member_titles):
        print(f"Warning: The number of items ({len(members)}) and item titles ({len(member_titles)}) doesn't match for page '{page_name}'.")
        member_titles = [None] * len(members)

    parsed_page_members: list[MemberItem] = []
    for member, member_title in zip(members, member_titles):
        member_name: str = ""
        member_type: str = ""
        member_doc: str = ""
        member_url: str = ""

        if member_title:
            if tag_a := member_title.find("a"):
                member_url = cast(str, tag_a.get("href", ""))

        if member_doc_html := member.find("div", class_ = EClassName.MEMBER_DOC):
            member_doc = docstring_markdown.description_to_markdown(str(member_doc_html))

        if table_name := member.find("table", class_ = EClassName.MEMBER_NAME):
            if table_name_data := table_name.find("td", class_ = EClassName.MEMBER_NAME):
                member_name = get_safe_text(table_name_data.get_text())
                if " " in member_name:
                    member_type, _, member_name = member_name.rpartition(" ")
                    member_name = member_name.strip()
                    member_type = member_type.strip()

                    # In 2024 `FBSystem::DesktopSize` type is broken and contains html code
                    if "</a>" in member_type:
                        member_type = member_type.rpartition("</a>")[2].strip()

            # Find all parameters
            parameters: list[Parameter] = []
            for table_row in table_name.find_all("tr"):
                table_data_type = table_row.find("td", class_ = EClassName.PARAMETER_TYPE)
                table_data_name = table_row.find("td", class_ = EClassName.PARAMETER_NAME)

                if table_data_name and table_data_type:
                    parameter_type = get_safe_text(table_data_type.get_text())
                    parameter_name = get_safe_text(table_data_name.get_text())

                    # the last param might have the end function ')' included
                    if (
                        parameter_name.endswith(")") and
                        parameter_name.count("(") < parameter_name.count(")")
                        ):
                        parameter_name = parameter_name[:-1].strip()

                    parameter_default_value = None
                    if "=" in parameter_name:
                        parameter_name, _, parameter_default_value = parameter_name.partition("=")

                        parameter_default_value = parameter_default_value.strip()
                        parameter_name = parameter_name.strip()

                    if not parameter_name:
                        if parameter_type.startswith("p"):
                            parameter_name = parameter_type
                            parameter_type = ""
                        else:
                            parameter_name = None

                    parameters.append(
                        Parameter(
                            parameter_name,
                            parameter_type,
                            parameter_default_value
                        )
                    )

        parsed_page_members.append(
            MemberItem(
                member_name,
                member_type,
                member_doc,
                parameters,
                member_url
            )
        )

    return ParsedPage(page_name, page_description.strip(), parsed_page_members)
