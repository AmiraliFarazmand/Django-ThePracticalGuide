from django.urls import path
from . import views
urlpatterns = [
    path('option1' , views.index) ,
    path('option2', views.index),
    path('option3', views.index2)
]
