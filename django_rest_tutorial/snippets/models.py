"""
Snippets Models Module

Description:
    - This module contains the models for the snippets app.

"""

from django.db.models import (
    BooleanField,
    CharField,
    DateTimeField,
    Model,
    TextField,
)
from pygments.lexers import get_all_lexers
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

    class Meta:
        """
        Meta Class

        Description:
            - This class is used to define metadata options for the Snippet
            model.

        Attributes:
            - `ordering (list[str])`: List of fields to order the queryset by.

        Methods:
            - `None`

        """

        ordering: list[str] = ["created"]
