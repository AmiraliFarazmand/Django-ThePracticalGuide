import re
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
# Create your views here.
views_dict ={
    'op1': 'op1 called !!',
    'op2': 'op2 called !!',
    'op3': 'op3 called !!',
    'op4': 'op4 called !!'
}
def allops_numbers(request , op):
    response_ls= list(views_dict.keys())
    return HttpResponseRedirect('/challenges_app/'+response_ls[op])

def allops (request , op): 
    if op in views_dict.keys():
        return HttpResponse(f'{views_dict[op]}  was called!!!')
    else:
        return HttpResponseNotFound(f'{op} was not found in urls!!!')