from django.http import HttpResponse
from django.shortcuts import render
from .models import Book, Review

# Create your views here.
def index(request):
    books = Book.objects.all().order_by('-posted_at')
    return render(request,'index.html',{'books':books})


def site_details(request):
  return render (request,'home.html')

def submit(request):
    return render(request,'submit.html')

def search(request):
    return render(request,'search.html')


