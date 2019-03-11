from django.urls import path , include
from . import views


urlpatterns = \
    [
        # added all paths edir and recipe details want to go to specific pages
        # so they need id numbers for specific recipes
        path('',views.index, name='index'),
        path('NewUser/',views.NewUser , name='NewUser'),
        path('NewRecipe/',views.NewRecipe , name='NewRecipe'),
        path('AllRecipes/',views.AllRecipes , name='AllRecipes'),
        path('ProfilePage/',views.ProfilePage , name='ProfilePage'),
        path('EditRecipe/<int:RecipeID>/',views.EditRecipe , name='EditRecipe'),
        path('RecipeDetails/<int:RecipeID>/',views.RecipeDetails , name='RecipeDetails'),
        path('accounts/', include('django.contrib.auth.urls')),
    ]