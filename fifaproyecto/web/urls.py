from django.urls import path , include
from . import views

urlpatterns = [
    path('', views.home, name='home'), # vISTA PRINCIPAL
    path('jugadores/', views.jugadores, name='jugadores'), # VISTA DE JUGADORES
    path('equipos/', views.equipos, name='equipos'), # VISTA DE EQUIPOS

]