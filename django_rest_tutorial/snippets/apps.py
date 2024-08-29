"""
Snippets Apps Module

Description:
    - This module contains the configuration for the snippets app.

"""

from django.apps import AppConfig


class SnippetsConfig(AppConfig):
    """
    Snippets Configuration Class

    Description:
        - This class contains the configuration for the snippets app.

    Attributes:
        - `default_auto_field (str)`: The default auto field for the app.
        - `name (str)`: The name of the app.

    Methods:
        - `None`

    """

    default_auto_field: str = "django.db.models.BigAutoField"
    name: str = "snippets"
