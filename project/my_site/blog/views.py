from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render ,get_object_or_404
from  datetime import date
from django.template.loader import render_to_string
from .models import Post
all_posts = [
        
]
# Create your views here.
def get_date(post):
    return post["date"]

'''Responde functions : ============================================================'''
def start_page(request):
    # sorted_posts =sorted(all_posts , key = get_date)
    # latest_posts = sorted_posts[-3:]
    # return render(request , './templates/blog/index.html')
    latest_posts = Post.objects.all().order_by("date")[:3]
    return render(request , 'blog/index.html' ,{
        "posts" : latest_posts})
    # return ('salam')

def posts_page(request):    
    all_posts = Post.objects.all()
    return render(request , 'blog/all-posts.html' , {"all_posts":all_posts})

def post_detail(request , slug):
    # specific_post = next(post for post in all_posts if slug ==post["slug"])
    # specific_post = Post.objects.get(slug=slug) 
    specific_post = get_object_or_404(Post , slug=slug)
    return render(request , 'blog/post_detail.html' ,{
        'post':specific_post ,
        "post_tags":specific_post.tag.all()
        })

def not_found(request , string):
    response  = render_to_string( '404.html')
    # raise Http404
    return HttpResponseNotFound(response)