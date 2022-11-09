from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("" , views.start_page , name="index"), 
    path("posts" , views.posts_page , name="all_posts"),
    path("posts/<slug:slug>" , views.post_detail , name="post_detail_page"),
    path("<str:string>" , views.not_found , name="not_found")
]+ static( settings.MEDIA_URL , document_root  =settings.MEDIA_ROOT)
