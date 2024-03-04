from django.urls import path

from .views import RecipeDetailView, RecipeListView

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe_detail'),
]

app_name = "ledger"