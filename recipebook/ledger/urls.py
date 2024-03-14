from django.urls import path

from .views import RecipeDetailView, RecipeListView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe_detail'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

app_name = "ledger"