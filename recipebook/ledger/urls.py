from django.urls import path

from .views import RecipeDetailView, RecipeListView, CustomLoginView, CustomPasswordResetView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('list/', RecipeListView.as_view(), name='recipe_list'),
    path('<int:pk>/detail', RecipeDetailView.as_view(), name='recipe_detail'),
    path('login/', CustomLoginView.as_view(), name='login.html'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]

app_name = "ledger"