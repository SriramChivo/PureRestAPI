from django.contrib import admin
from django.urls import path, re_path
from .views import ListApiView

urlpatterns = [
    path('Common/', ListApiView.as_view(), name="List"),
]
