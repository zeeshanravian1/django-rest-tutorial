"""
Snippets Views Module

Description:
    - This module contains the views for the snippets app.

"""

from typing import Sequence

from django.contrib.auth.models import User
from django.db.models import Manager, QuerySet
from rest_framework.decorators import api_view
from rest_framework.generics import (
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly,
    OperandHolder,
    SingleOperandHolder,
)
from rest_framework.renderers import BaseRenderer, StaticHTMLRenderer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer


@api_view(["GET"])
def api_root(
    request: Request,
    format: str | None = None,  # pylint: disable=redefined-builtin
) -> Response:
    """
    API Root Function

    Description:
        - This function is used to display the API root.

    Args:
        - `request (Request)`: The request object. **(Required)**
        - `format (str)`: The format of the request. **(Optional)**

    Returns:
        - `Response`: The response object.

    """

    return Response(
        {
            "users": reverse(
                viewname="user-list", request=request, format=format
            ),
            "snippets": reverse(
                viewname="snippet-list", request=request, format=format
            ),
        }
    )


class SnippetHighlight(GenericAPIView):
    """
    Snippet Highlight Class

    Description:
        - This class defines the view for the Snippet Highlight.

    Attributes:
        - `queryset (QuerySet[Snippet] | Manager[Snippet] | None)`: The
        queryset that will be used to retrieve the Snippet objects.
        - `renderer_classes (Sequence[type[BaseRenderer]])`: The renderer
        classes that will be used to render the Snippet objects.

    Methods:
        - `get`: The get method that will be used to get the Snippet object.

    """

    queryset: QuerySet[Snippet] | Manager[Snippet] | None = (  # type: ignore
        Snippet.objects.all()  # pylint: disable=no-member
    )
    renderer_classes: Sequence[type[BaseRenderer]] = [StaticHTMLRenderer]

    def get(
        self,
        request: Request,  # pylint: disable=unused-argument
        *args,  # pylint: disable=unused-argument
        **kwargs,  # pylint: disable=unused-argument
    ) -> Response:
        """
        Get Method

        Description:
            - This method is used to get the Snippet object.

        Args:
            - `request (Request)`: The request object. **(Required)**
            - `args`: The arguments. **(Optional)**
            - `kwargs`: The keyword arguments. **(Optional)**

        Returns:
            - `Response`: The response object.

        """

        snippet: Snippet = self.get_object()
        return Response(data=snippet.highlighted)


class UserList(ListAPIView):
    """
    User List Class

    Description:
        - This class defines the view for the User List.

    Attributes:
        - `queryset (QuerySet[User] | Manager[User] | None)`: The queryset
        that will be used to retrieve the User objects.
        - `serializer_class (UserSerializer)`: The serializer class that will
        be used to serialize the User objects.

    Methods:
        - `None`

    """

    queryset: QuerySet[User] | Manager[User] | None = (  # type: ignore
        User.objects.all()  # pylint: disable=no-member
    )
    serializer_class = UserSerializer


class UserDetail(RetrieveAPIView):
    """
    User Detail Class

    Description:
        - This class defines the view for a single User object.

    Attributes:
        - `queryset (QuerySet[User] | Manager[User] | None)`: The queryset
        that will be used to retrieve the User objects.
        - `serializer_class (UserSerializer)`: The serializer class that will
        be used to serialize the User objects.

    Methods:
        - `None`

    """

    queryset: QuerySet[User] | Manager[User] | None = (  # type: ignore
        User.objects.all()  # pylint: disable=no-member
    )
    serializer_class = UserSerializer


class SnippetList(ListCreateAPIView):
    """
    Snippet List Class

    Description:
        - This class defines the view for the Snippet List.

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
    permission_classes: list[  # type: ignore
        type[BasePermission] | OperandHolder | SingleOperandHolder
    ] = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer) -> None:
        """
        Perform the creation of a Snippet object.

        Description:
            - This method is used to create a Snippet object

        Args:
            - `serializer (SnippetSerializer)`: The serializer that will be
            used to create the Snippet object. **(Required)**

        Returns:
            - `None`

        """

        serializer.save(owner=self.request.user)


class SnippetDetail(RetrieveUpdateDestroyAPIView):
    """
    Snippet Detail Class

    Description:
        - This class defines the view for a single Snippet object.

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
    permission_classes: list[  # type: ignore
        type[BasePermission] | OperandHolder | SingleOperandHolder
    ] = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
