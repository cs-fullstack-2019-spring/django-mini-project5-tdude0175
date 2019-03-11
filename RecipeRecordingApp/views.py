from django.shortcuts import render , redirect , get_object_or_404
from .forms import RecipeModel , RecipeForm, RecipeMakerModel , RecipeMakerForm
from django.contrib.auth.models import User
# Create your views here.

# I used single function for all data saves for ease

# this renders all recipes if the person is logged in otherwise it will just load the page
def index(request):
    if request.user.is_authenticated:
        RecipeList = RecipeModel.objects.filter(CreatorOfRecipe__Name = request.user)
        context = \
            {
                'RecipeList':RecipeList
            }
        return render(request,'RecipeRecordingApp/index.html',context)

    return render(request,'RecipeRecordingApp/index.html')

# for making a new user it also makes the model and the user and link them via foreign key
def NewUser(request):
    form = RecipeMakerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        newUser =  User.objects.create_user(request.POST['Name'],request.POST['EmailAddress'],request.POST['Password'])
        userForm= form.save(commit=False)
        userForm.UserLink =newUser
        userForm.save()
        return redirect('index')
    context = \
        {
            'form':form
        }
    return render(request,'RecipeRecordingApp/NewUser.html',context)

# This will let you make a new recipe and link it the same way that a new user is created
def NewRecipe(request):
    form = RecipeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        RecipeMaker = RecipeMakerModel.objects.get(UserLink = request.user)
        saveRecipe = form.save(commit=None)
        saveRecipe.CreatorOfRecipe = RecipeMaker
        saveRecipe.save()
        return redirect('index')
    context =\
        {
            'form':form
        }
    return render(request,'RecipeRecordingApp/NewRecipe.html',context)


# simply gathers all recipes made and renders them for selected and then you can click them to go to the details page
def AllRecipes(request):
    Recipes = RecipeModel.objects.all()
    context = \
        {
            'AllRecipes':Recipes
        }
    return render(request,'RecipeRecordingApp/AllRecipes.html',context)


# view a persons profile and lets you edit them on the bottom of the page
def ProfilePage(request):
    personLoggedIn= get_object_or_404(RecipeMakerModel,Name=request.user)
    userPage = User.objects.get(username = request.user)
    MakerForm = RecipeMakerForm(request.POST or None ,instance=personLoggedIn)
    if request.method == 'POST' and MakerForm.is_valid():
        editedInfo = MakerForm.save()
        userPage.username = request.POST['Name']
        userPage.save()
        context= \
            {
                'ModelItems':personLoggedIn,
                'form':MakerForm
            }
        return render(request,'RecipeRecordingApp/ProfilePage.html',context)

    context=\
        {
            'ModelItems':personLoggedIn,
            'form':MakerForm
        }
    return render(request,'RecipeRecordingApp/ProfilePage.html',context)


# Edit a recipe is made when you populate on the home page so it can pass the information
# using the id number of the recipe
def EditRecipe(request,RecipeID):
    recipe = get_object_or_404(RecipeModel, pk = RecipeID)
    form = RecipeForm( request.POST or None , instance=recipe)
    if request.method == 'POST'and form.is_valid():
        form.save()
        return redirect('index')
    return render(request,'RecipeRecordingApp/EditRecipe.html',{'form':form})


# renders the page with only details of the recipe to be viewed
def RecipeDetails(request,RecipeID):
    recipe = get_object_or_404(RecipeModel, pk = RecipeID)
    context =\
        {
            'Recipe':recipe
        }
    return render(request,'RecipeRecordingApp/DetailsPage.html',context)
