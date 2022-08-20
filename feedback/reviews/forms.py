from  django import forms

class ReviewForm(forms.Form):   
    # username = forms.CharField()
    username = forms.CharField(max_length=50 , min_length=4)
    