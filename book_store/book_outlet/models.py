from urllib import request
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    author = models.TextField(null=True , blank=True)
    top_selling  = models.BooleanField(default=False )
    slug = models.SlugField(default="" , null=False  , blank=True )

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     super().save(*args, **kwargs)
        
    def get_detailed(self):
        return reverse("book_detail", args=[self.slug])
        
    def __str__(self) -> str:
        return f"title:{self.title} , rate:{self.rate} "
    