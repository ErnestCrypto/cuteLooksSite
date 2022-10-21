from django.contrib import admin
from django.urls import path
from . import views

app_name = "siteAppUrls"


urlpatterns = [
    path('/', views.indexPage, name="indexPage"),
]
