"""
Snippets Views Module

Description:
    - This module contains the views for the snippets app.

"""

from django.db.models import Manager, QuerySet
from rest_framework import generics, mixins
from rest_framework.request import Request
from rest_framework.response import Response

from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(
    mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView
):
    """
    Snippet List Class

    Description:
        - This class defines the view for the Snippet model.

    Args:
        - `mixins.ListModelMixin`: A mixin class that provides a `list` method.
        - `mixins.CreateModelMixin`: A mixin class that provides a `create`
        method.
        - `generics.GenericAPIView`: A generic class-based view that provides
        the core functionality.

    Attributes:
        - `queryset (QuerySet[Snippet] | Manager[Snippet] | None)`: The
        queryset that will be used to retrieve the Snippet objects.
        - `serializer_class (SnippetSerializer)`: The serializer class that
        will be used to serialize the Snippet objects.

    Methods:
        - `get`: Retrieves a list of Snippet objects.
        - `post`: Creates a new Snippet object.

    """

    queryset: QuerySet[Snippet] | Manager[Snippet] | None = (  # type: ignore
        Snippet.objects.all()  # pylint: disable=no-member
    )
    serializer_class = SnippetSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Get Method

        Description:
            - This method retrieves a list of Snippet objects.

        Args:
            - `request (Request)`: The request object. **(Required)**
            - `*args`: Variable length argument list. **(Optional)**
            - `**kwargs`: Arbitrary keyword arguments. **(Optional)**

        Returns:
            - `Response`: The response object.

        """

        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs) -> Response:
        """
        Post Method

        Description:
            - This method creates a new Snippet object.

        Args:
            - `request (Request)`: The request object. **(Required)**
            - `*args`: Variable length argument list. **(Optional)**
            - `**kwargs`: Arbitrary keyword arguments. **(Optional)**

        Returns:
            - `Response`: The response object.

        """

        return self.create(request, *args, **kwargs)


class SnippetDetail(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView,
):
    """
    Snippet Detail Class

    Description:
        - This class defines the view for a single Snippet object.

    Args:
        - `mixins.RetrieveModelMixin`: A mixin class that provides a `retrieve`
        method.
        - `mixins.UpdateModelMixin`: A mixin class that provides an `update`
        method.
        - `mixins.DestroyModelMixin`: A mixin class that provides a `destroy`
        method.
        - `generics.GenericAPIView`: A generic class-based view that provides
        the core functionality.

    Attributes:
        - `queryset (QuerySet[Snippet] | Manager[Snippet] | None)`: The
        queryset that will be used to retrieve the Snippet objects.
        - `serializer_class (SnippetSerializer)`: The serializer class that
        will be used to serialize the Snippet objects.

    Methods:
        - `get`: Retrieves a single Snippet object.
        - `put`: Updates a single Snippet object.
        - `delete`: Deletes a single Snippet object.

    """

    queryset: QuerySet[Snippet] | Manager[Snippet] | None = (  # type: ignore
        Snippet.objects.all()  # pylint: disable=no-member
    )
    serializer_class = SnippetSerializer

    def get(self, request: Request, *args, **kwargs) -> Response:
        """
        Get Method

        Description:
            - This method retrieves a single Snippet object.

        Args:
            - `request (Request)`: The request object. **(Required)**
            - `*args`: Variable length argument list. **(Optional)**
            - `**kwargs`: Arbitrary keyword arguments. **(Optional)**

        Returns:
            - `Response`: The response object.

        """
        return self.retrieve(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs) -> Response:
        """
        Put Method

        Description:
            - This method updates a single Snippet object.

        Args:
            - `request (Request)`: The request object. **(Required)**
            - `*args`: Variable length argument list. **(Optional)**
            - `**kwargs`: Arbitrary keyword arguments. **(Optional)**

        Returns:
            - `Response`: The response object.

        """

        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs) -> Response:
        """
        Delete Method

        Description:
            - This method deletes a single Snippet object.

        Args:
            - `request (Request)`: The request object. **(Required)**
            - `*args`: Variable length argument list. **(Optional)**
            - `**kwargs`: Arbitrary keyword arguments. **(Optional)**

        Returns:
            - `Response`: The response object.

        """

        return self.destroy(request, *args, **kwargs)
