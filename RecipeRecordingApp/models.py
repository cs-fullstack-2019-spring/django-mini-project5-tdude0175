from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class RecipeMakerModel(models.Model):
    Name = models.CharField(max_length=100)
    Password = models.CharField(max_length=200)
    EmailAddress = models.EmailField()
    ProfilePicture = models.URLField(max_length=500)
    UserLink = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name

class RecipeModel(models.Model):
    PictureOfMeal= models.URLField(max_length=500)
    NameOfMeal=models.CharField(max_length=100)
    IngredientsForMeal=models.CharField(max_length=500)
    DirectionsForMeal=models.TextField(max_length=500)
    DateCreated=models.DateField(default=timezone.now)
    CreatorOfRecipe= models.ForeignKey(RecipeMakerModel, on_delete=models.PROTECT)

    def __str__(self):
        return self.NameOfMeal
