from django.contrib import admin
from .models import Book ,Author , Address

# Register your models here.

class BookAdmin(admin.ModelAdmin):
    # readonly_fields= ("slug", )
    prepopulated_fields= {"slug":("title" , )}
    list_display = ("title" , "author" , "rate" , )
    list_filter = ("rate" ,)
    list_per_page= 5
    ordering= ("-rate", )

class AuthorAdmin(admin.ModelAdmin):
    list_display=("id" ,"first_name" , "last_name" ,)


admin.site.register(Book ,BookAdmin)
admin.site.register(Author)
admin.site.register(Address)