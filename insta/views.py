from django.shortcuts import render
from django.http  import HttpResponse
from .models import Images
from django.contrib.auth.decorators import login_required
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Myinsta app')

@login_required(login_url='/accounts/login/')
def index(request):
    photo = Images.objects.all().order_by('-id')

    return render(request, 'all-insta/index.html',{'photo':photo})