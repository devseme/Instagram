from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Myinsta app')
def index(request):
    return render(request, 'all-insta/index.html')