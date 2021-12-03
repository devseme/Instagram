from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True, default='No bio')
    profile = models.ImageField(upload_to='images/', default='default.jpeg')
    
    def save_profile(self):
        self.save()


class Images(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    
    def save_images(self):
        self.save()

     
    def delete_images(self):
        self.delete()
     # update photos
    # def update_images(self, name, def update_images(self, name, description,category,location):
    #     self.name = name
    #     self.description = description
    #     self.category = category
    #     self.location =location
    #     self.save()description,category,location):
    #     self.name = name
    #     self.description = description
    #     self.category = category
    #     self.location =location
    #     self.save()

    def _str_(self):
        return self.name
        

        


   
    
    
  