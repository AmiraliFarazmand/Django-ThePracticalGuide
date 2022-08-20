from django.shortcuts import render
from django.http import HttpResponseRedirect

# Create your views here.

def review (request):
    if request.method == "POST":
        users_input = request.POST["username"]
        print(users_input , "***")
        return HttpResponseRedirect("/thank-you")
    
    return render(request ,template_name='reviews/review.html')

def thank_you (request ):    
    return render(request , "reviews/thank_you.html" )