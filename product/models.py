from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

class Drink(models.Model):
    name = models.CharField(max_length=20)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    nutrient = models.TextField()
    allergy = models.TextField()



