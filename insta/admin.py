from django.contrib import admin
from .models import Comments, Images,Profile,Likes

# Register your models here.
admin.site.register(Images)
admin.site.register(Profile)
admin.site.register(Likes)
admin.site.register(Comments)