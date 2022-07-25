from doctest import REPORT_CDIFF
import re
from urllib import response
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string
# Create your views here.
views_dict ={
    'op1': 'op1 called ! ! :))))))))))',
    'op2': 'op2 called @@@@@@@@@',
    'op3': 'op3 called $$$$$$$$',
    'op4': 'op4 called !!!!!!!!!!!',
    'op5' : None,
    'op6': ' op6 is some different op',
}
def allops_numbers(request , op):
    try:
        response_ls= list(views_dict.keys())
        redirect_elm =response_ls[op-1]
        redirect_path = reverse('reverse_challange' ,args=[redirect_elm])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound('not found :(')

def allops (request , op): 
    try:
        challenge = views_dict[op]
        # response_data = render_to_string('challenges_app/challenge.html')
        # return HttpResponse(response_data)
        response_data = render(request ,'challenges_app/challenge.html' , {'op_key' : op , 'op_value': challenge})
        return response_data
    except:
        return HttpResponseNotFound(f'<h3>{op} was not found in urls!!!(we\'re in allops function)</h3>')

def index_func(request ):
    keys_ls  = list(views_dict.keys())
    # res_str = ''
    # for key in keys_ls:
    #     op_path = reverse('reverse_challange',args=[key])
    #     pth = f"<li><a href=\"{op_path}\">{key} </a></li>"
    #     res_str+=pth
    # response= f'<ul>{res_str}</ul>'
    return render(request ,'challenges_app/index.html', {'op_list': keys_ls})