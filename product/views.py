from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def index(request):
    products=Product.objects.all()#return all the product from our database
    #There are other object. methods based on your needs
    return render(request,'index.html',#render the html 
    {'products':products})#the dictionary associates elements of the displayed list with elements of our database

def new(request):
 
    return HttpResponse('New Products')