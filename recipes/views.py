from django.views import generic
from django.shortcuts import render , reverse
from .models import Recipe
from .forms import CustomUserCreationForm

# Create your views here.

class LandingPageView(generic.TemplateView):
    template_name = "landing.html"
    
class RecipesListView(generic.ListView):
    template_name = "recipes/recipes_list.html"
    queryset = Recipe.objects.all()
    context_object_name = "recipes"
    
class RecipeDetailView(generic.DetailView):
    template_name="recipes/recipes_detail.html"
    context_object_name = "recipes"
    
    def get_queryset(self , *args , **kwargs):
        return Recipe.objects.filter(id=self.kwargs['pk'])

class SignupView(generic.CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm

    def get_success_url(self):
        return reverse("login")

    

        
    
