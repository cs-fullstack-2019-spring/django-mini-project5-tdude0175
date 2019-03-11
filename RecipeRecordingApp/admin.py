from django.contrib import admin
from .forms import RecipeModel, RecipeMakerModel
# Register your models here.


admin.site.register(RecipeMakerModel)
admin.site.register(RecipeModel)