from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.PokemonList.as_view(), name = 'lista_pokemon'),
    path('crear_pokemon/', views.PokemonCreate.as_view(), name = 'crear_pokemon'),
    path('editar_pokemon/<int:pk>/', views.PokemonUpdate.as_view(), name = 'editar_pokemon'),
    path('borrar_pokemon/', views.PokemonDelete, name = 'borrar_pokemon'),
]