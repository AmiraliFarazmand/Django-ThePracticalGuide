from django.shortcuts import render

# Create your views here.

def start_page(request):
    # return render(request , './templates/blog/index.html')
    return render(request , 'blog/index.html')
    # return ('salam')

def posts_page(request):    
    return render(request , 'blog/all-posts.html')

def post_detail(request , slug):
    return render(request , 'blog/post_detail.html')