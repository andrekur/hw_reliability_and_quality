from rest_framework import routers
from django.urls import path, include

from .views import *

urlpatterns = [
    path('v1/get_levin_len/', API_Levin.as_view()),
]
