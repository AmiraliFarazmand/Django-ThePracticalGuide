from tabnanny import verbose
from tkinter import CASCADE
from urllib import request
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    postal_card= models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.city + ' - ' + self.street+' | '+self.postal_card
    class Meta:
        verbose_name_plural = "addresses"
        
        
class Author(models.Model):
    first_name = models.CharField(max_length=100 )
    last_name = models.CharField(max_length=100 )
    address = models.OneToOneField(Address,null=True ,on_delete=models.CASCADE ,)  
    def __str__(self):
        return f" {self.first_name}-{self.last_name}"
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    rate = models.IntegerField(default=0 ,validators=[MaxValueValidator(5) , MinValueValidator(0)])
    # author = models.TextField(null=True , blank=True)
    author = models.ForeignKey(Author ,on_delete =models.CASCADE , null=True , related_name="books" )
    top_selling  = models.BooleanField(default=False )
    slug = models.SlugField(default="" , null=False  , blank=True )

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
        
    def get_detailed(self):
        return reverse("book_detail", args=[self.slug])
        
    def __str__(self) -> str:
        return f"{self.id}|{self.title} [{self.author}] ({self.rate}) "
    