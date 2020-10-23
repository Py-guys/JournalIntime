from django.contrib import admin
from django.urls import path
from journal import views

urlpatterns = [
    path("",views.index,name="index"),
    path('/downloads', views.download_file, name="Wouhoo")
]