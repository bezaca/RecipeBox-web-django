from django import forms
from .models import Recipe
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm , UsernameField


User = get_user_model()

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = "__all__"

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {"username": UsernameField}