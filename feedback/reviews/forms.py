from cProfile import label
from  django import forms

class ReviewForm(forms.Form):   
    # username = forms.CharField()
    username = forms.CharField(max_length=50 , min_length=4 ,required=True , label="Username" ,error_messages={
        "max_length":"Enter a shorter name!" ,
        "required": "This field must be filled!" }
                                )
    email   = forms.EmailField(label="Email", required=False)
    review_text = forms.CharField(label="Your review", max_length=200, required=False ,widget=forms.Textarea)
    rating = forms.IntegerField(label="Rating",min_value=0 , max_value=4)