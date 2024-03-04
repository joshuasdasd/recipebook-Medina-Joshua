from django.db import models
from django.urls import reverse

# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=100)
                            
    def __str__(self):
        return self.name

class Recipe(models.Model):
    name = models.CharField(max_length=100)

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