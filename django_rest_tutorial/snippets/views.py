"""
Snippets Views Module

Description:
    - This module contains the views for the snippets app.

"""

from django.contrib.auth.models import User
from django.db.models import Manager, QuerySet
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action, api_view
from rest_framework.permissions import (
    BasePermission,
    OperandHolder,
    SingleOperandHolder,
)
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


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.

    """

    queryset: QuerySet[User] | Manager[User] | None = (  # type: ignore
        User.objects.all()  # pylint: disable=no-member
    )
    serializer_class = UserSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    This ViewSet automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.

    """

    queryset: QuerySet[Snippet] | Manager[Snippet] | None = (  # type: ignore
        Snippet.objects.all()  # pylint: disable=no-member
    )
    serializer_class = SnippetSerializer
    permission_classes: list[  # type: ignore
        type[BasePermission] | OperandHolder | SingleOperandHolder
    ] = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly,
    ]

    @action(
        methods=["GET"],
        detail=True,
        renderer_classes=[renderers.StaticHTMLRenderer],
    )
    def highlight(
        self,
        request: Request,  # pylint: disable=unused-argument
        *args,  # pylint: disable=unused-argument
        **kwargs,  # pylint: disable=unused-argument
    ) -> Response:
        """
        Highlight Action

        Description:
            - This action is used to highlight a snippet.

        Args:
            - `request (Request)`: The request object. **(Required)**
            - `args`: Additional arguments. **(Optional)**
            - `kwargs`: Additional keyword arguments. **(Optional)**

        Returns:
            - `Response`: The response object.

        """
        snippet: Snippet = self.get_object()

        return Response(snippet.highlighted)

    def perform_create(self, serializer) -> None:
        """
        Perform Create Method

        Description:
            - This method is used to perform the create operation.

        Args:
            - `serializer`: The serializer object. **(Required)**

        Returns:
            - `None`

        """

        serializer.save(owner=self.request.user)
