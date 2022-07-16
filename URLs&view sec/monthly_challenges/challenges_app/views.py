import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
# Create your views here.
views_dict ={
    'op1': 'op1 called !!',
    'op2': 'op2 called !!',
    'op3': 'op3 called !!',
    'op4': 'op4 called !!'
}
def allops_numbers(request , op):
    response_ls= list(views_dict.keys())
    redirect_elm =response_ls[op-1]
    redirect_path = reverse('reverse_challange' ,args=[redirect_elm])
    return HttpResponseRedirect(redirect_path)

def allops (request , op): 
    if op in views_dict.keys():
        return HttpResponse(f'<h1>{views_dict[op]}  was called!!!</h1>')
    else:
        return HttpResponseNotFound(f'<h3>{op} was not found in urls!!!</h3>')