from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from .models import Pokemon 
from django.urls import reverse_lazy
from .forms import PokemonForm
from django.http import HttpResponse

# Create your views here.

class PokemonList(ListView):
    template_name = "pokapp/lista_pokemon.html"
    model = Pokemon

class PokemonCreate(CreateView):
    template_name = "pokapp/crear_pokemon.html"
    model = Pokemon
    fields = '__all__'
    success_url = reverse_lazy('lista_pokemon')

class PokemonUpdate(UpdateView):
    template_name = "pokapp/actualizar_pokemon.html"
    model = Pokemon
    form_class = PokemonForm
    success_url = reverse_lazy('lista_pokemon')

def PokemonDelete(request):
    if request.is_ajax:
        if request.method == 'POST':
            id = request.POST.get('id')
            borrar = Pokemon.objects.get(id=id)
            borrar.delete()
            return HttpResponse('Ok')
    return HttpResponse('Fallido')


"""class PokemonDelete(DeleteView):
    #template_name = "pokapp/borrar_pokemon.html"
    template_name = "pokapp/lista_pokemon.html"    
    model = Pokemon
    succes_url = reverse_lazy('lista_pokemon')"""