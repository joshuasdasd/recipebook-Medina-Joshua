from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Recipe


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'ledger/recipe_details.html'
        