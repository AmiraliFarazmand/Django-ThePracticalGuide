from  django import forms

class ReviewForm(forms.Form):   
    # username = forms.CharField()
    username = forms.CharField(max_length=50 , min_length=4 ,required=True , label="USERNAME" ,error_messages={
        "max_length":"Enter a shorter name!" ,
        "required": "This field must be filled!" }
                                )
