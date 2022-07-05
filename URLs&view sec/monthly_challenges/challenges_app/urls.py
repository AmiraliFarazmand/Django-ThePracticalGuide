from django.urls import path
from . import views

urlpatterns = [
path('<int:op>' , views.allops_numbers),
path('<str:op>' , views.allops),
]
