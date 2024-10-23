from django.urls import path
from .views import get_home_page, get_bmi_page, get_chatbot_page

urlpatterns = [
    path('', get_home_page),
    path('bmi', get_bmi_page),
    path('chatbot', get_chatbot_page)
]
