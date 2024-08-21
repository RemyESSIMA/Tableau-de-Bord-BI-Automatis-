# TableauDeBordBI/Tableau/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL pour l'interface d'administration Django
    path('', include('dashboard.urls')),  # Inclure les routes définies dans 'dashboard/urls.py'
]
