from django.shortcuts import render
from .models import Book
from django.http import Http404
# Create your views here.


def index(request):
    all_books = Book.objects.all()
    return render(request, "book_outlet/index.html" , { "books": all_books })

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