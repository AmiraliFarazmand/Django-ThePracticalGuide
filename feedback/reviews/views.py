from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm 

# Create your views here.

def review (request):
    if request.method == "POST":
    #     users_input = request.POST["username"]
    #     print(users_input , "***")
        form = ReviewForm(request.POST)
        if form.is_valid():
            print(form.clean() ,"###")
            return HttpResponseRedirect("/thank-you")
    
    form = ReviewForm(request.POST)
    return render(request ,'reviews/review.html',
                {"form": form} ,
                )

def thank_you (request ):    
    return render(request , "reviews/thank_you.html" )