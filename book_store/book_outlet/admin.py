from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields= ("slug", )
    prepopulated_fields= {"slug":("title" , )}
    list_display = ("title" , "author" , "rate" , )
    list_filter = ("rate" ,)
    list_per_page= 5
    ordering= ("-rate", )

admin.site.register(Book ,BookAdmin)