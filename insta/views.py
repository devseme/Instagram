from django.shortcuts import render,redirect, get_object_or_404
from django.http  import HttpResponse,HttpResponseRedirect
from .models import Images,Profile,Likes
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import UserForm



@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    # get images for the current logged in user
    image = Images.objects.filter(user_id=current_user.id)
    # get the profile of the current logged in user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    form = UserForm()
    if request.method == 'POST':
        form = UserForm (request.POST , request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
        redirect('profile')

        

    return render(request, 'profile.html', {"image": image, "profile": profile,"form": form})


# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Myinsta app')

@login_required(login_url='/accounts/login/')
def index(request):
    photo = Images.objects.all().order_by('-id')
    user = request.user.id

    context ={
        'photo':photo,
        'user':user,
    }
    return render(request, 'all-insta/index.html',context)

def like_image(request):
    user = request.user
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image_pic =Images.objects.get(id=image_id)
        if user in image_pic.liked.all():
            image_pic.liked.add(user)
        else:
            image_pic.liked.add(user)    
            
        like,created =Likes.objects.get_or_create(user=user, image_id=image_id)
        if not created:
            if like.value =='Like':
               like.value = 'Unlike'
        else:
               like.value = 'Like'

        like.save()       
    return redirect('index')