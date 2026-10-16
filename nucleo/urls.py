from django.urls import path

from .views import home, criar_colaborador, editar_colaborador, excluir_colaborador

urlpatterns = [
    path('', home, name='home'),
    path('novo/', criar_colaborador, name='criar_colaborador'),
    path('editar/<int:pk>/', editar_colaborador, name='editar_colaborador'),
    path('excluir/<int:pk>/', excluir_colaborador, name='excluir_colaborador'),
]
