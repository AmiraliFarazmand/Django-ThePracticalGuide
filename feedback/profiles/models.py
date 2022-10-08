from django.db import models

# Create your models here.

class UserProfileModel(models.Model):   
    image = models.FileField(upload_to= "profile_images")