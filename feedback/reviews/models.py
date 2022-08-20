from django.db import models
from django.core.validators import MaxValueValidator , MinValueValidator

# Create your models here.

class Review(models.Model): 
    username = models.CharField(max_length=50)
    email = models.EmailField(null=True , max_length=50)
    review = models.TextField(null=True , max_length=200)
    rating = models.IntegerField(null=False , default=3 ,validators = [MinValueValidator(0) ,MaxValueValidator(5)])
    admin_comment = models.CharField(max_length=100, null=True)