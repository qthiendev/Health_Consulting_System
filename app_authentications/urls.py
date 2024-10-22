from django.urls import path
from .views import get_login, get_logout, get_register

urlpatterns = [
    path('login/', get_login, name='login'),
    path('logout/', get_logout, name='logout'),
    path('register/', get_register, name='register'),
]
