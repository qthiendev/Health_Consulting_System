from django.contrib import admin
from django.urls import path

from app_utilities import views as utilities

from app_authentications import views as authentications

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', utilities.get_home),
    path('login', authentications.get_login),
]
