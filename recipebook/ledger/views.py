from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models import Recipe
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordResetView


# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'ledger/recipe_details.html'

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset_form.html'
    