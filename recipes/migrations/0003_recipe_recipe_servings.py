# Generated by Django 3.1.7 on 2021-02-26 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_recipe_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='Recipe_Servings',
            field=models.TextField(default='', max_length=20),
        ),
    ]