from django.urls import path

from . import views

urlpatterns = [
path("", views.names, name="names"),
path("index/", views.index, name="index"),
path("kwame/", views.kwame, name="kwame"),

]