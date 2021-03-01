from django.urls import path

from .views import (
    RecipesListView,
    RecipeDetailView
)

app_name = 'recipes'

urlpatterns = [
    path("" , RecipesListView.as_view() , name='recipes-list' ),
    path('<int:pk>/', RecipeDetailView.as_view(), name='recipes-detail'),

]


