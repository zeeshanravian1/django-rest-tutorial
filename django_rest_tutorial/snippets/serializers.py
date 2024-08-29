"""
Snippets Serializers Module

Description:
    - This module contains the serializers for the snippets app.

"""

from django.contrib.auth.models import User
from rest_framework.serializers import (
    ManyRelatedField,
    ModelSerializer,
    PrimaryKeyRelatedField,
    ReadOnlyField,
    RelatedField,
)

from .models import Snippet


class UserSerializer(ModelSerializer):
    """
    User Serializer Class

    Description:
        - This class is used to serialize the User model.

    Attributes:
        - `snippets (list[Snippet])`: The snippets of the user.

    Methods:
        - `None`

    """

    snippets: RelatedField[Snippet, Snippet, Snippet] | ManyRelatedField = (
        PrimaryKeyRelatedField(
            many=True,
            queryset=Snippet.objects.all(),  # pylint: disable=no-member
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
        fields: list[str] = ["id", "username", "snippets"]


class SnippetSerializer(ModelSerializer):
    """
    Snippet Serializer Class

    Description:
        - This class is used to serialize the Snippet model.

    Attributes:
        - `owner (str)`: The owner of the snippet.

    Methods:
        - `None`

    """

    owner = ReadOnlyField(source="owner.username")

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
            "id",
            "title",
            "code",
            "linenos",
            "language",
            "style",
            "owner",
        ]
