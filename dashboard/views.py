# dashboard/views.py

from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd
import plotly.express as px
from io import BytesIO
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
from django.shortcuts import render


# Vue pour gérer l'upload de fichiers
def upload_file(request):
    if request.method == 'POST':
        # Vérifiez si un fichier a été téléchargé
        if 'file' in request.FILES:
            # Lire le fichier en utilisant Pandas
            file = request.FILES['file']
            df = pd.read_csv(file)

            # Stockez le DataFrame dans la session pour l'utiliser plus tard
            request.session['data'] = df.to_dict()

            # Affiche les premières lignes des données
            context = {'columns': df.columns, 'rows': df.head().values}
            return render(request, 'dashboard/data_uploaded.html', context)

    return render(request, 'dashboard/upload.html')


# Vue pour afficher le tableau de bord
def dashboard_view(request):
    # Récupérer les données stockées dans la session
    data = request.session.get('data', None)

    if data:
        # Convertir les données en DataFrame
        df = pd.DataFrame.from_dict(data)

        # Création d'un graphique avec Plotly
        fig = px.bar(df, x=df.columns[0], y=df.columns[1])
        graph = fig.to_html(full_html=False)

        return render(request, 'dashboard/dashboard.html', {'graph': graph})

    return HttpResponse("Aucune donnée disponible. Veuillez d'abord télécharger un fichier.")


# Vue pour générer un rapport PDF
def generate_report(request):
    # Récupérer les données stockées dans la session
    data = request.session.get('data', None)

    if data:
        df = pd.DataFrame.from_dict(data)

        # Générer un PDF avec Matplotlib
        buffer = BytesIO()
        with PdfPages(buffer) as pdf:
            plt.figure(figsize=(8, 6))
            plt.plot(df[df.columns[0]], df[df.columns[1]])
            plt.title('Graphique des Données')
            plt.xlabel(df.columns[0])
            plt.ylabel(df.columns[1])
            pdf.savefig()  # Sauvegarder la figure dans le PDF
            plt.close()

        buffer.seek(0)
        return HttpResponse(buffer, as_attachment=True, content_type='application/pdf')

    return HttpResponse("Aucune donnée disponible pour générer le rapport.")

def home_view(request):
    return render(request, 'home.html')  # Créer un template home.html ou en utiliser un existant


def some_other_view(request):
    return render(request, 'dashboard/Upload.html')  # Exemple de vue pour un autre template
