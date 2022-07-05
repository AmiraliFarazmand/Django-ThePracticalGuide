import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound
# Create your views here.

def allops (request , op): 
    if op =='op1'or op =='op2' or op =='op3':
        return HttpResponse(f'{op} was called!!!')
    else:
        return HttpResponseNotFound(f'{op} was not found in urls!!!')