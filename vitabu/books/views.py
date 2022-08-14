from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Review

# Create your views here.
def index(request):
    books = Book.objects.all()
    return render(request,'index.html',{'books':books})

def home(request):
  return render (request,'home.html')

def submit(request):
    return render(request,'submit.html')

def search(request):
    return render(request,'search.html')

def rate(request):
    return render('site_details',id)


