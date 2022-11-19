from django.forms import Form ,ModelForm
from . import models


class CommentForm(ModelForm):
        class Meta:
            model = models.Comment
            fields = "__all__"
            exclude =["post" , ]
            labels = {"content" :"Your comment" , "shown_name": "Your name" , "owner_email" : "Your email" ,}