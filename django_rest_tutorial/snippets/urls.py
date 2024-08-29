"""
Snippet URLs Module

Description:
    - This module contains the URL configuration for the snippets app.

"""

from django.urls import path
from django.urls.resolvers import URLPattern, URLResolver
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns: list[URLPattern | URLResolver] = [
    path(route="", view=views.snippet_list),
    path(route="<int:pk>/", view=views.snippet_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)
