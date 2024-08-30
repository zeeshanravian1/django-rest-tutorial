"""
Snippets Serializers Module

Description:
    - This module contains the serializers for the snippets app.

"""

from django.contrib.auth.models import User
from rest_framework.serializers import (
    Hyperlink,
    HyperlinkedIdentityField,
    HyperlinkedModelSerializer,
    HyperlinkedRelatedField,
    ManyRelatedField,
    ReadOnlyField,
    RelatedField,
)

from .models import Snippet


class UserSerializer(HyperlinkedModelSerializer):
    """
    User Serializer Class

    Description:
        - This class is used to serialize the User model.

    Attributes:
        - `snippets (RelatedField[Snippet, str, Hyperlink] | ManyRelatedField)`
        : The snippets of the user.

    Methods:
        - `None`

    """

    snippets: RelatedField[User, str, Hyperlink] | ManyRelatedField = (
        HyperlinkedRelatedField(
            many=True, view_name="snippet-detail", read_only=True
        )
    )

    class Meta:  # type: ignore
        """
        User Meta Class

        Description:
            - This class contains metadata for the `UserSerializer` class.

        Attributes:
            - `model (type[User])`: The model that the serializer is based on.
            - `fields (list[str])`: The fields that the serializer should
            include.

        Methods:
            - `None`

        """

        model: type[User] = User
        fields: list[str] = ["url", "id", "username", "snippets"]


class SnippetSerializer(HyperlinkedModelSerializer):
    """
    Snippet Serializer Class

    Description:
        - This class is used to serialize the Snippet model.

    Attributes:
        - `owner (str)`: The owner of the snippet.
        - `highlight (RelatedField[Snippet, str, Hyperlink] |
        ManyRelatedField)`: The highlight of the snippet.

    Methods:
        - `None`

    """

    owner = ReadOnlyField(source="owner.username")
    highlight: RelatedField[Snippet, str, Hyperlink] | ManyRelatedField = (
        HyperlinkedIdentityField(view_name="snippet-highlight", format="html")
    )

    class Meta:  # type: ignore
        """
        Snippet Meta Class

        Description:
            - This class contains metadata for the `SnippetSerializer` class.

        Attributes:
            - `model (type[Snippet])`: The model that the serializer is based
            on.
            - `fields (list[str])`: The fields that the serializer should
            include.

        Methods:
            - `None`

        """

        model: type[Snippet] = Snippet
        fields: list[str] = [
            "url",
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
            "highlight",
        ]
