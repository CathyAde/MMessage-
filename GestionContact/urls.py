# GestionContact/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.gerer_contact, name='gerer_contact'),
    path('create/', views.create_contact, name='create_contact'),
    path('update/<int:pk>/', views.update_contact, name='update_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
]
