"""
Snippet Permissions Module

Description:
    - This module contains the permissions for the snippets app.

"""

from typing import Literal

from rest_framework.permissions import SAFE_METHODS, BasePermission
from rest_framework.request import Request


class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.

    """

    def has_object_permission(
        self, request: Request, view, obj
    ) -> Literal[True]:
        """
        Check if the user has permission to access the object.

        Args:
            - `request (Request)`: The request object. **(Required)**
            - `view`: The view object. **(Required)**
            - `obj`: The object to check permissions for. **(Required)**

        Returns:
            - `Literal[True]`: Whether the user has permission to access the
            object.

        """
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user
