from django.contrib import admin
from django.urls import path

from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_utilities.urls')),
    path('auth/', include('app_authentications.urls')),
    path('user/', include('app_users.urls')),
]
