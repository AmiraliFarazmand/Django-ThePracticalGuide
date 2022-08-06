from django.shortcuts import render

# Create your views here.

def start_page(request):
    # return render(request , './templates/blog/index.html')
    return render(request , 'blog/index.html')
    # return ('salam')

def posts_page(request):    
    return 'salam'

def post_detail(request):
    pass