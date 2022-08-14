from django.shortcuts import render
from .models import Book
from django.http import Http404
from django.db.models import Avg , Max
# Create your views here.


def index(request):
    all_books = Book.objects.all().order_by("-rate") 
    count = all_books.count()
    avg_rate = all_books.aggregate(Avg("rate"))
    return render(request, "book_outlet/index.html" , { "books": all_books ,
                                                        "count" :count,
                                                        "avg_rate" :avg_rate,
                                                        })

def book_detail(request , slug ):
    try:
        book = Book.objects.get(slug=slug)
        return render(request, "book_outlet/book_detail.html" , { 
                                                    "title": book.title, 
                                                    "book": book.title ,  
                                                    "author" : book.author , 
                                                    "rate" : book.rate, 
                                                    "top_selling": book.top_selling ,
                                                    })
    except :
        raise Http404