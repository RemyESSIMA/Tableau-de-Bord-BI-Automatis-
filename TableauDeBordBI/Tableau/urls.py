# TableauDeBordBI/Tableau/urls.py

from django.contrib import admin
from django.urls import path, include

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),  # Inclut les URLs de l'application dashboard
    path('', include('dashboard.urls')),  # Pour la route par défaut
]
