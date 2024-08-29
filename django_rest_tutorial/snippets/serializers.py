"""
Snippets Serializers Module

Description:
    - This module contains the serializers for the snippets app.

"""

from rest_framework.serializers import ModelSerializer

from .models import Snippet


class SnippetSerializer(ModelSerializer):
    """
    Snippet Serializer Class

    Description:
        - This class is used to serialize the Snippet model.

    Attributes:
        - `id (int)`: The id of the snippet.
        - `title (str)`: The title of the snippet.
        - `code (str)`: The code of the snippet.
        - `linenos (bool)`: The line numbers of the snippet.
        - `language (str)`: The language of the snippet.
        - `style (str)`: The style of the snippet.

    Methods:
        - `None`

    """

    class Meta:  # type: ignore
        """
        Snippet Meta Class

        Description:
            - This class contains metadata for the `SnippetSerializer` class.

        Attributes:
            - `model (Model)`: The model that the serializer is based on.
            - `fields (list[str])`: The fields that the serializer should
            include.

        Methods:
            - `None`

        """

        model: type[Snippet] = Snippet
        fields: list[str] = [
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
        ]
