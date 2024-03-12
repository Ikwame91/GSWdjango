from django.urls import path

from . import views

urlpatterns = [
# path("", views.names, name="names"),
path("names/", views.names, name="names"),
path("names/details/<int:id>", views.details, name="details"),


path("index/", views.index, name="index"),
path("kwame/", views.kwame, name="kwame"),

]