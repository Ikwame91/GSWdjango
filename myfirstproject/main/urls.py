from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name = "index"),
    path("f1/", views.f1, name = "forum 1"),
]