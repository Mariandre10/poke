from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PokemonList(TemplateView):
    template_name = "pokapp/lista_pokemon.html"
