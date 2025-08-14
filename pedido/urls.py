from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('olhar_produtos/', views.olhar_produtos, name='olhar_produtos'),
    path('adicionarNoCarrinho/<str:pk>/', views.adicionarNoCarrinho, name='adicionarNoCarrinho'),
    path('delete/<str:pk>/', views.deletar, name='deletar_prod'),
    path('diminuir/<str:pk>/', views.diminuir, name='diminuir_prod'),
    path('aumentar/<str:pk>/', views.aumentar, name='aumentar_prod'),
    path('verPedido/<str:pk>/', views.verPedido, name='verPedido'),
    path('finalizar/', views.finalizar, name='finalizar'),
    path('pedidos_anteriores/', views.pedidos_anteriores, name='pedidos_anteriores'),
    #path('editar/<str:pk>/', views.editar, name='editar_prod'),
]