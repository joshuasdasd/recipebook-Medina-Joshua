from django.urls import path

from .views import RecipeDetailView, RecipeListView, CustomLoginView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe_detail'),
    path('login/', CustomLoginView.as_view(), name='login.html'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

app_name = "ledger"