from django.urls import path
from . import views 



urlpatterns = [
path('', views.index_func , name='index'),
path('<int:op>' , views.allops_numbers ,name='reverse_challange'),
path('<str:op>' , views.allops ,name = 'reverse_challange'),
]