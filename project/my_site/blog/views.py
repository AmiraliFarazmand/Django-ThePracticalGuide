from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render ,get_object_or_404
from  datetime import date
from django.template.loader import render_to_string

from django.views.generic import ListView , DetailView

from .forms import CommentForm
from .models import Post
all_posts = [
        
]
# Create your views here.
# def get_date(post):
#     return post["date"]

'''Responde functions : ============================================================'''
# def start_page(request):
#     # sorted_posts =sorted(all_posts , key = get_date)
#     # latest_posts = sorted_posts[-3:]
#     # return render(request , './templates/blog/index.html')
#     latest_posts = Post.objects.all().order_by("date")[:3]
#     return render(request , 'blog/index.html' ,{
#         "posts" : latest_posts})
#     # return ('salam')
class StartPageView (ListView):
    model = Post
    template_name = "blog/index.html"
    ordering = ["-date" ,]
    context_object_name = "posts"
    def get_queryset(self):
        all = super().get_queryset()
        data = all[:3]
        return data
        
# def posts_page(request):    
#     all_posts = Post.objects.all()
#     return render(request , 'blog/all-posts.html' , {"all_posts":all_posts})
class AllPostsView(ListView):
    model = Post
    ordering = ["-date" , "title" , ]
    context_object_name ="all_posts"
    template_name = "blog/all-posts.html"
    
    
# def post_detail(request , slug):
#     # specific_post = next(post for post in all_posts if slug ==post["slug"])
#     # specific_post = Post.objects.get(slug=slug) 
#     specific_post = get_object_or_404(Post , slug=slug)
#     return render(request , 'blog/post_detail.html' ,{
#         'post':specific_post ,
#         "post_tags":specific_post.tag.all()
#         })
class PostDetailView(DetailView):
    model  = Post
    template_name = "blog/post_detail.html"
    def get_context_data(self, **kwargs):
        data =  super().get_context_data(**kwargs)
        data["post_tags"] = self.object.tag.all()
        data["comment_form" ] = CommentForm() 
        return data
    
def not_found(request , string):
    response  = render_to_string( '404.html')
    # raise Http404
    return HttpResponseNotFound(response)