from django import forms
from .models import RecipeMakerModel , RecipeModel


class RecipeMakerForm(forms.ModelForm):
    class Meta:
        model = RecipeMakerModel
        exclude = ['UserLink',]


class RecipeForm(forms.ModelForm):
    class Meta:
        model = RecipeModel
        exclude =['CreatorOfRecipe']
