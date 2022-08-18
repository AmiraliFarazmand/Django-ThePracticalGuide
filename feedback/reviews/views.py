from http.client import HTTPResponse
from django.shortcuts import render

# Create your views here.

def review (request):
    return render(request ,template_name='review.html')