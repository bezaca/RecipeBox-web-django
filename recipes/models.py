from django.db import models
from django.contrib.auth.models import AbstractUser

class Recipe(models.Model):

    Recipe_Title = models.CharField(max_length=200)
    Recipe_Description = models.TextField(default='' , max_length=500)
    Recipe_Image = models.ImageField(upload_to="recipes/" , default="dummy.png")
    Recipe_Servings = models.TextField(max_length=20 , default='')
    Recipe_Ingredients = models.TextField(default='' , max_length=500  )
    Recipe_Preparation = models.TextField(default='' , max_length=1000 )
    Owner = models.ForeignKey("User" , on_delete=models.SET_NULL , null=True)

    def __str__(self):
        return f'{self.Recipe_Title}'

class User(AbstractUser):
    
    def __str__(self):
        return f'{self.username}'