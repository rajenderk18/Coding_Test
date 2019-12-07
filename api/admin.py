from django.contrib import admin
from api.models import  Step, Ingredient, Recipe


#Model registration 


admin.site.register(Step)
admin.site.register(Ingredient)
admin.site.register(Recipe)