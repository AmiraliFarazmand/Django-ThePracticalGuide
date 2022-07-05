import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse 
# Create your views here.

def index (request): 
    return HttpResponse("first view!!!") 

def index2(request):
    return HttpResponse("second view!!!")
