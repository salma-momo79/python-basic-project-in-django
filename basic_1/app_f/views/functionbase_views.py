from django.shortcuts import render , redirect, get_object_or_404
from ..models import book
from app_f.models import book

# def book_list(request):
#     books = book.objects.all()
#     context = {
#         'books' : books,
#         'massage': 'This is Function base views'
#     }
#     return render(request,'books/book_list.html',context)
def book_list(request):
    Model = book_list
    HTML = book.objects.all()
    return render (request,'book_list.html')

def Coverpage(request):
    Model = coverpage
    HTML = book.objects.all()
    return render (request , 'Cover_Page.html')