# TableauDeBordBI/urls.py

from django.contrib import admin
from django.urls import path, include
from dashboard.views import home_view  # Importer la vue

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),  # Inclure les URLs du module 'dashboard'
    path('', home_view, name='home'),  # Assigner la vue home_view à la racine
]
