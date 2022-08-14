from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path(""  , views.index ), 
    path("<slug:slug>" , views.book_detail , name="book_detail") ,
]
