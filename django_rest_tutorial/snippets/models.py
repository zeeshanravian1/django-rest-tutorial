"""
Snippets Models Module

Description:
    - This module contains the models for the snippets app.

"""

from typing import Literal

from django.db.models import (
    CASCADE,
    BooleanField,
    CharField,
    DateTimeField,
    ForeignKey,
    Model,
    TextField,
)
from pygments import highlight
from pygments.formatters.html import HtmlFormatter
from pygments.lexer import Lexer
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles

LEXERS: list[tuple[str, tuple[str, ...], tuple[str, ...], tuple[str, ...]]] = [
    item for item in get_all_lexers() if item[1]
]
LANGUAGE_CHOICES: list[tuple[str, str]] = sorted(
    [(item[1][0], item[0]) for item in LEXERS]
)
STYLE_CHOICES: list[tuple[str, str]] = sorted(
    [(item, item) for item in get_all_styles()]
)


class Snippet(Model):
    """
    Snippet Model

    Description:
        - This model is used to represent a code snippet.

    Attributes:
        - `created (DateTimeField)`: Date and time the snippet was created.
        - `title (CharField)`: Title of the snippet.
        - `code (TextField)`: Code of the snippet.
        - `linenos (BooleanField)`: Whether to display line numbers in the
        snippet.
        - `language (CharField)`: Language of the snippet.
        - `style (CharField)`: Style of the snippet.
        - `owner (ForeignKey)`: The owner of the snippet.
        - `highlighted (TextField)`: The highlighted HTML representation of the
        snippet.

    Methods:
        - `None`

    """

    created: DateTimeField = DateTimeField(auto_now_add=True)
    title: CharField = CharField(max_length=100, blank=True, default="")
    code: TextField = TextField()
    linenos: BooleanField = BooleanField(default=False)
    language: CharField = CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style: CharField = CharField(
        choices=STYLE_CHOICES, default="friendly", max_length=100
    )
    owner: ForeignKey = ForeignKey(
        to="auth.User", related_name="snippets", on_delete=CASCADE
    )
    highlighted: TextField = TextField()

    class Meta:
        """
        Meta Class

        Description:
            - This class is used to define metadata options for the Snippet
            model.

        Attributes:
            - `ordering (list[str])`: List of fields to order the queryset by.

        Methods:
            - `save(*args, **kwargs) -> None`: Save the snippet to the
            database.

        """

        ordering: list[str] = ["created"]

    def save(self, *args, **kwargs) -> None:
        """
        Use the `pygments` library to create a highlighted HTML
        representation of the code snippet.
        """
        lexer: Lexer = get_lexer_by_name(_alias=self.language)
        linenos: Literal["table"] | Literal[False] = (
            "table" if self.linenos else False
        )
        options: dict[str, str] = {"title": self.title} if self.title else {}
        formatter: HtmlFormatter = HtmlFormatter(  # type: ignore
            style=self.style,
            linenos=linenos,
            full=True,
            **options,  # type: ignore
        )

        self.highlighted = highlight(
            code=self.code, lexer=lexer, formatter=formatter
        )
        super().save(*args, **kwargs)
