from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    short_bio = models.TextField()

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
                            
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)

    ingredient = models.ForeignKey(
        Ingredient, 
        related_name='recipe', 
        on_delete=models.CASCADE
    )

    recipe = models.ForeignKey(
        Recipe, 
        related_name='ingredients', 
        on_delete=models.CASCADE
    )

    def get_absolute_url(self):
        return reverse('recipeingredient_detail', args=[str(self.quantity)])

    def __str__(self):
        return f"{self.quantity} of {self.ingredient.name} for {self.recipe.name}"