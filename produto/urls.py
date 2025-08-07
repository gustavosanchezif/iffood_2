from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('adicionar/', views.adicionar, name='adicionar_prod'),
    path('delete/<str:pk>/', views.deletar, name='deletar_prod'),
    path('editar_form/<str:pk>/', views.editar_form, name='editar_form_prod'),
    path('editar/<str:pk>/', views.editar, name='editar_prod'),
]