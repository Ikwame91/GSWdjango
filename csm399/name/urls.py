from django.urls import path

from . import views

urlpatterns = [
path("", views.main, name="main"),
path("names/", views.names, name="names"),
path("names/details/<int:id>", views.details, name="details"),
path("testing/", views.testing, name="testing"),
path("test/", views.test, name="test"),

path("index/", views.index, name="index"),
path("kwame/", views.kwame, name="kwame"),

]