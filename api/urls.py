from django.contrib import admin
from django.urls import path, include
from api import views

urlpatterns = [

    path('recipes/<int:recipe_id>', views.RecipesView.as_view(), name='id-recipes'),
    path('recipes/', views.RecipesView.as_view(), name='all-recipes'),
    
]


