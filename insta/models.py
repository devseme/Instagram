from django.db import models

from cloudinary.models import CloudinaryField

# Create your models here.

class Images(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=250, blank=True)
    caption = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
   
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
        

        


   
    
    
  