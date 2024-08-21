# dashboard/urls.py  hhhhh

from django.urls import path
from .views import upload_file, dashboard_view, generate_report

urlpatterns = [
    path('upload/', upload_file, name='upload_file'),  # Route pour le formulaire d'upload
    path('dashboard/', dashboard_view, name='dashboard_view'),  # Route pour le tableau de bord
    path('report/', generate_report, name='generate_report'),  # Route pour générer le rapport PDF
]
