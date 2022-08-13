from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    author = models.TextField(null=True , blank=True)
    top_selling  = models.BooleanField(default=False )
    
    def __str__(self) -> str:
        return f"title:{self.title} , rate:{self.rate} "