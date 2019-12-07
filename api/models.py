from rest_framework import serializers
from django.db import models




#Recipe model 

class Recipe(models.Model):
    name = models.CharField(max_length=500)
    user = models.OneToOneField( "User", on_delete=models.CASCADE, primary_key=True,)
    

class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recipe
        exclude = ()        


#Ingredient model

class Ingredient(models.Model):
    text = models.CharField(max_length=500)
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE)
    

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        exclude = ()


#Step model

class Step(models.Model):
    step_text = models.CharField(max_length=500)
    recipe = models.ForeignKey("Recipe", on_delete=models.CASCADE, default="dinner")
   

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        exclude = ()
