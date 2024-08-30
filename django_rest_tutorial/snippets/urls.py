"""
Snippet URLs Module

Description:
    - This module contains the URL configuration for the snippets app.

"""

from django.urls import path
from django.urls.resolvers import URLPattern, URLResolver
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# API endpoints
urlpatterns: list[URLPattern | URLResolver] = format_suffix_patterns(
    [
        path(route="", view=views.api_root),
        path(
            route="snippets/",
            view=views.SnippetList.as_view(),
            name="snippet-list",
        ),
        path(
            route="snippets/<int:pk>/",
            view=views.SnippetDetail.as_view(),
            name="snippet-detail",
        ),
        path(
            route="snippets/<int:pk>/highlight/",
            view=views.SnippetHighlight.as_view(),
            name="snippet-highlight",
        ),
        path(route="users/", view=views.UserList.as_view(), name="user-list"),
        path(
            route="users/<int:pk>/",
            view=views.UserDetail.as_view(),
            name="user-detail",
        ),
    ]
)
