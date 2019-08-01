from django import forms
from .models import Pokemon

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = ('__all__')
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'id':'inputEmail3', 'name':'name', 'placeholder':'Nombre'}),
            'specie': forms.TextInput(attrs={'class':'form-control', 'id':'inputPassword3', 'name':'specie', 'placeholder':'Especie'}),
            'description': forms.TextInput(attrs={'class':'form-control', 'id':'inputPassword4', 'name':'descrption', 'placeholder':'Descripcion'}),
            'tipo': forms.TextInput(attrs={'class':'form-control', 'id':'inputPassword4', 'name':'tipo', 'placeholder':'Tipo'}),
            'photo': forms.TextInput(attrs={'class':'form-control', 'id':'inputPassword4', 'name':'photo', 'placeholder':'url'})
        }