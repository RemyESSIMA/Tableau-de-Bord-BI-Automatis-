# TableauDeBordBI/Tableau/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),  # Inclure les URLs du module 'dashboard'
]
