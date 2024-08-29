"""
Snippets Views Module

Description:
    - This module contains the views for the snippets app.

"""

from django.db.models import Manager, QuerySet
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(ListCreateAPIView):
    """
    Snippet List Class

    Description:
        - This class defines the view for the Snippet List.

    Args:
        - `ListCreateAPIView`: A generic class-based view that provides the
        core functionality.

    Attributes:
        - `queryset (QuerySet[Snippet] | Manager[Snippet] | None)`: The
        queryset that will be used to retrieve the Snippet objects.
        - `serializer_class (SnippetSerializer)`: The serializer class that
        will be used to serialize the Snippet objects.

    Methods:
        - `None`

    """

    queryset: QuerySet[Snippet] | Manager[Snippet] | None = (  # type: ignore
        Snippet.objects.all()  # pylint: disable=no-member
    )
    serializer_class = SnippetSerializer


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    """
    Snippet Detail Class

    Description:
        - This class defines the view for a single Snippet object.

    Args:
        - `RetrieveUpdateDestroyAPIView`: A generic class-based view that
        provides the core functionality.

    Attributes:
        - `queryset (QuerySet[Snippet] | Manager[Snippet] | None)`: The
        queryset that will be used to retrieve the Snippet objects.
        - `serializer_class (SnippetSerializer)`: The serializer class that
        will be used to serialize the Snippet objects.

    Methods:
        - `None`

    """

    queryset: QuerySet[Snippet] | Manager[Snippet] | None = (  # type: ignore
        Snippet.objects.all()  # pylint: disable=no-member
    )
    serializer_class = SnippetSerializer
