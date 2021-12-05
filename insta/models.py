from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_photo = CloudinaryField('image')
    bio = models.TextField(max_length=500, blank=True, null=True)
    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile

    def _str_(self):
        return self.user.username

class Images(models.Model):
    image = CloudinaryField('image')
    name = models.CharField(max_length=250, blank=True)
    liked= models.ManyToManyField(User,default=None,blank=True,related_name='liked')
    caption = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(auto_now_add=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', null=True)
    

    @property
    def num_likes(self):
        return self.liked.all().count()

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

class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    comment = models.CharField(max_length=50)
    comm_date = models.DateTimeField(auto_now_add=True)

    def save_comment(self):
        self.save()
    
    def delete_comment(self):
        self.delete()

    def __str__(self):
        return self.user

LIKE_CHOICES={
    ('Like','Like'),
    ('Unlike','Unlike',)
}
class Likes(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,default='like',max_length=10)

    def __str__(self):
        return self.user

          
        

        


   
    
    
  