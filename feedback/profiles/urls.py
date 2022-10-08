from django.urls import path

from . import views

urlpatterns = [
    path("", views.CreateProfileView.as_view()),
    path("all" , views.AllProfilesView.as_view()),
]
