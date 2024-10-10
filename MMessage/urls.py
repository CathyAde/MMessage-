from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Authentification
    path('auth/', include('Authentification.urls')),
    path('auth/', include('social_django.urls', namespace='social')),
    
    # Gestion des contacts
    path('contacts/', include('GestionContact.urls')),
    
    # Page d'accueil
    path('', include('Authentification.urls')),  # Redirection vers Authentification pour la page d'accueil
]