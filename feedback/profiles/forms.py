from django import  forms

class ProfileForm(forms.Form):
    profile_image = forms.ImageField(allow_empty_file=False , required=True )