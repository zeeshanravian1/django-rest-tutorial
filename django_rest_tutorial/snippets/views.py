"""
Snippets Views Module

Description:
    - This module contains the views for the snippets app.

"""

from django.contrib.auth.models import User
from django.db.models import Manager, QuerySet
from rest_framework.generics import (
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

from .models import Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import SnippetSerializer, UserSerializer


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
            used to create the Snippet object.

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
