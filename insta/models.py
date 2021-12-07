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

    def delete_profile(self):
        self.delete()

    def save_profile(self):
        self.save() 

    def delete_profile(self):
        self.delete()

    def update_image(self, user_id, new_image):
        user = User.objects.get(id = user_id)
        self.photo = new_image 
        self.save()

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

    @property
    def saved_comments(self):
        return self.comments.all()    

    def save_images(self):
        self.save()
    
     
    def delete_images(self):
        self.delete()

    @classmethod
  # search images using image name
    def search_image_name(cls, search_term):
        images = cls.objects.filter(
        name__icontains=search_term)
        return images    

    def _str_(self):
        return self.user.username       

    def _str_(self):
        return self.name



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
        return self.value

          
class Comments(models.Model):
    comment = models.CharField(max_length=250)
    image = models.ForeignKey(Images,on_delete = models.CASCADE,related_name='comments')
    user = models.ForeignKey(User,on_delete = models.CASCADE,related_name='comments')

    @classmethod
    def display_comment(cls,image_id):
        comments = cls.objects.filter(image_id = image_id)
        return comments


   
    
    
  