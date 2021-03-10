from django.urls import path

from .views import *

urlpatterns = [
    path('v1/get_levin_len/', API_Levin.as_view()),
]
