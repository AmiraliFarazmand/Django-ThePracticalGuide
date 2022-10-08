from cProfile import label
from  django import forms

from .models import Review
# class ReviewForm(forms.Form):   
#     # username = forms.CharField()
#     username = forms.CharField(max_length=50 , min_length=4 ,required=True , label="Username" ,error_messages={
#         "max_length":"Enter a shorter name!" ,
#         "required": "This field must be filled!" }
#                                 )
#     email   = forms.EmailField(label="Email", required=False)
#     review_text = forms.CharField(label="Your review", max_length=200, required=False ,widget=forms.Textarea)
#     rating = forms.IntegerField(label="Rating",min_value=0 , max_value=4)
    

class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields="__all__"
        exclude= ["admin_comment",]
        labels={"username":"Your username", 
                "email":"Your email address" ,
                "rating":"Your rating",
                }