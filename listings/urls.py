from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="list"),
    path("create", views.create, name="create"),
    path("<int:id>", views.detail, name="detail"),
    path("<int:id>/update", views.update, name="update"),
    path("<int:id>/delete", views.delete, name="delete"),
    path("search", views.search, name="search"),
]
