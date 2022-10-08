from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect

from .forms import ProfileForm
# Create your views here.

def store(file):
    with open("temp/img.jpg" ,"wb") as dest:
        for chunk in file.chunks():
            dest.write(chunk)
    
class CreateProfileView(View):
    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form" : form})

    def post(self, request):
        # img = request.FILES["image"]
        # print(img , "***")
        # store(img)
        submitted_form  =ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            store(request.FILES["profile_image"])
            return HttpResponseRedirect("/profiles")        
        else:
            return render(request, "profiles/create_profile.html" , {"form":submitted_form})