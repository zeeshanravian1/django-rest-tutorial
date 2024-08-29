"""
Snippets Views Module

Description:
    - This module contains the views for the snippets app.

"""

from django.db.models import QuerySet
from django.http import Http404
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(APIView):
    """
    List all snippets, or create a new snippet.

    """

    def get(self, request: Request, format=None) -> Response:
        """
        List all code snippets.

        Description:
            - This method returns all code snippets in the database.

        Args:
            - `request (Request)`: The request object.  **(Required)**
            - `format (str)`: The format of the response.  **(Optional)**

        Returns:
            - `Response`: The response object containing the serialized
            snippets.

        """
        snippets: QuerySet[Snippet] = (  # type: ignore
            Snippet.objects.all()  # pylint: disable=no-member
        )
        serializer: SnippetSerializer = SnippetSerializer(
            instance=snippets, many=True
        )
        return Response(data=serializer.data)

    def post(self, request: Request, format=None) -> Response:
        """
        Create a new code snippet.

        Description:
            - This method creates a new code snippet in the database.

        Args:
            - `request (Request)`: The request object.  **(Required)**
            - `format (str)`: The format of the response.  **(Optional)**

        Returns:
            - `Response`: The response object containing the serialized
            snippet.

        """

        serializer: SnippetSerializer = SnippetSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()
        return Response(data=serializer.data, status=status.HTTP_201_CREATED)


class SnippetDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.

    """

    def get_object(self, pk) -> Snippet:
        """
        Retrieve a snippet instance.

        Description:
            - This method retrieves a single snippet instance from the
            database.

        Args:
            - `pk (int)`: The primary key of the snippet.  **(Required)**

        Returns:
            - `Snippet`: The snippet instance.

        """

        try:
            return Snippet.objects.get(pk=pk)  # pylint: disable=no-member

        except Snippet.DoesNotExist as exc:  # pylint: disable=no-member
            raise Http404 from exc

    def get(self, request, pk, format=None) -> Response:
        """
        Retrieve a snippet instance.

        Description:
            - This method retrieves a snippet instance from the database.

        Args:
            - `request (Request)`: The request object.  **(Required)**
            - `pk (int)`: The primary key of the snippet.  **(Required)**
            - `format (str)`: The format of the response.  **(Optional)**

        Returns:
            - `Response`: The response object containing the serialized
            snippet.

        """

        snippet: Snippet = self.get_object(pk=pk)
        serializer: SnippetSerializer = SnippetSerializer(instance=snippet)

        return Response(data=serializer.data)

    def put(self, request, pk, format=None) -> Response:
        """
        Update a snippet instance.

        Description:
            - This method updates a snippet instance in the database.

        Args:
            - `request (Request)`: The request object.  **(Required)**
            - `pk (int)`: The primary key of the snippet.  **(Required)**
            - `format (str)`: The format of the response.  **(Optional)**

        Returns:
            - `Response`: The response object containing the serialized
            snippet.

        """
        snippet: Snippet = self.get_object(pk=pk)
        serializer: SnippetSerializer = SnippetSerializer(
            instance=snippet, data=request.data
        )

        if not serializer.is_valid():
            return Response(
                data=serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        serializer.save()

        return Response(data=serializer.data)

    def delete(self, request, pk, format=None) -> Response:
        """
        Delete a snippet instance.

        Description:
            - This method deletes a snippet instance from the database.

        Args:
            - `request (Request)`: The request object.  **(Required)**
            - `pk (int)`: The primary key of the snippet.  **(Required)**
            - `format (str)`: The format of the response.  **(Optional)**

        Returns:
            - `Response`: The response object containing the serialized
            snippet.

        """
        snippet: Snippet = self.get_object(pk)
        snippet.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
