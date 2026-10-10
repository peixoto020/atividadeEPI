from django.urls import path
from . import views  # Importa as views do seu app nucleo

urlpatterns = [
    path('', views.home)
]