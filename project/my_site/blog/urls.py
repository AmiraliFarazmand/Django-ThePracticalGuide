from django.urls import path
from . import views
urlpatterns = [
    path("" , views.start_page , name="index"), 
    path("posts" , views.posts_page , name="all_posts"),
    path("posts/<slug:slug>" , views.post_detail , name="post_detail_page")
]
