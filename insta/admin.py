from django.contrib import admin
from .models import Comment, Images,Profile,Likes

# Register your models here.
admin.site.register(Images)
admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comment)