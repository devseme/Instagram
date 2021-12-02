from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images

# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Myinsta app')
    
def index(request):
    photo = Images.objects.all().order_by('-id')

    return render(request, 'all-insta/index.html',{'photo':photo})