from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Review
from django.http import Http404
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def index(request):
    return render(request,'base.html')

def home(request):
    books = Book.objects.all()
    return render (request,'home.html',{'books':books})


def search(request):
    return render(request, 'search.html')




