"""
Snippets Views Module

Description:
    - This module contains the views for the snippets app.

"""

from django.db.models import QuerySet
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializer


@api_view(["GET", "POST"])  # type: ignore
def snippet_list(request: Request) -> Response | None:
    """
    List all code snippets, or create a new snippet.

    """

    if request.method == "GET":
        snippets: QuerySet[Snippet] = (  # type: ignore
            Snippet.objects.all()
        )  # pylint: disable=no-member
        serializer: SnippetSerializer = SnippetSerializer(
            instance=snippets, many=True
        )
        return Response(data=serializer.data)

    elif request.method == "POST":
        serializer = SnippetSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])  # type: ignore
def snippet_detail(request, pk) -> Response | None:
    """
    Retrieve, update or delete a code snippet.

    """
    try:
        snippet: Snippet = Snippet.objects.get(  # pylint: disable=no-member
            pk=pk
        )

    except Snippet.DoesNotExist:  # pylint: disable=no-member
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serializer = SnippetSerializer(instance=snippet)
        return Response(data=serializer.data)

    elif request.method == "PUT":
        serializer = SnippetSerializer(instance=snippet, data=request.data)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(data=serializer.data)

    elif request.method == "DELETE":
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
