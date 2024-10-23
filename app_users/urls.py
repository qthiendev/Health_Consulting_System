# app_users/urls.py
from django.urls import path
from .views import edit_profile, get_profile

urlpatterns = [
    path('profile/edit/', edit_profile),
    path('profile/', get_profile),
]
