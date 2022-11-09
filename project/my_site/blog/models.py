from django.db import models

from django.core.validators import MinLengthValidator
# Create your models here.

class Author(models.Model): 
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    
    def __str__(self) -> str:
        return f"{self.first_name}-{self.last_name}[{self.id}]"
# --------------------------------------------------------------------------------------
class Tag(models.Model):
    captions = models.CharField(max_length=20)
    
    def __str__(self) -> str:
        return f"[{self.id}](C:{self.captions})"
# --------------------------------------------------------------------------------------
class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=200)
    content = models.TextField(max_length=5000 ,validators=[MinLengthValidator(limit_value=10)])
    # image_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "uploads" , null = True)
    date= models.DateField(auto_now=True)
    # slug = models.CharField(max_length=50)
    slug = models.SlugField(db_index=True , unique=True )  
    author = models.ForeignKey(Author ,on_delete=models.SET_NULL ,null=True  ,related_name="posts")
    tag = models.ManyToManyField(Tag)
    
    def __str__(self) -> str:
        return f"[{self.id}]-T:{self.title}-A:{self.author}"