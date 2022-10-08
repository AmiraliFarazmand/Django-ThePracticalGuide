from django import  forms

class ProfileForm(forms.Form):
    profile_image = forms.FileField(allow_empty_file=False , required=True )