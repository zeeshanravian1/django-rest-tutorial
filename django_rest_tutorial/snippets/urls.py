"""
Snippet URLs Module

Description:
    - This module contains the URL configuration for the snippets app.

"""

from django.urls import include, path
from django.urls.resolvers import URLResolver
from rest_framework.routers import DefaultRouter

from . import views

# Create a router and register our ViewSets with it.
router: DefaultRouter = DefaultRouter()
router.register(
    prefix=r"snippets", viewset=views.SnippetViewSet, basename="snippet"
)
router.register(prefix=r"users", viewset=views.UserViewSet, basename="user")

# The API URLs are now determined automatically by the router.
urlpatterns: list[URLResolver] = [
    path("", include(router.urls)),
]
