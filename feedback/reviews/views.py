from django import views
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View 
from django.views.generic  import TemplateView

from .forms import ReviewForm 
from .models import Review

# Create your views here.

# def review (request):
#     if request.method == "POST":
#     #     users_input = request.POST["username"]
#     #     print(users_input , "***")
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # print(form.clean() ,"###")
#             # rw=form.cleaned_data
#             # review = Review(username=rw["username"],email=rw["email"], review=rw["review"], rating= rw["rating"])
#             # review.save()
#             # print('done', rw)
#             form.save()
#             return HttpResponseRedirect("/thank-you")

#     else :
#         form = ReviewForm()

#     return render(request ,'reviews/review.html',
#                 {"form": form} ,
#                 )
# -----------------------------------------------------------------------------------------
class ReviewView(View):
    def post(self ,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect("/thank-you")
        else:
            return render(request ,'reviews/review.html',
                {"form": form} ,
                )
    def get(self,request):
        form = ReviewForm()
        return render(request ,'reviews/review.html',
                {"form": form} ,
                )
# ----------------------------------------------------------------------------------------

# def thank_you (request ):    
#     return render(request , "reviews/thank_you.html" )
class thank_youView(TemplateView):
    template_name: str = "reviews/thank_you.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["test"] = "it works!"
        return context
    