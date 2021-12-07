from django.test import TestCase
from .models import Comment, Images,Profile,Likes,User
import datetime as dt
# Create your tests here.
class ImagesTestCase(TestCase):
    def setUp(self):
        # create a user
        user = User.objects.create(
            username='test_user',
            first_name='ian',
            last_name='seme'
        )
        Images.objects.create(
            name='test_image',
            image='"https://cdn.pixabay.com/photo/2017/09/03/17/26/woman-2711279__340.jpg"',
            caption='test image',
        )
    def test_name(self):
        image = Images.objects.get(name='test_image')
        self.assertEqual(image.name, 'test_image')

class ProfileTestCase(TestCase):
    def setUp(self):
        user = User.objects.create(
            username='test_user',
            first_name='ian',
            last_name='seme'
        )
        Profile.objects.create(
            bio='test bio',
            profile_photo='https://unsplash.com/photos/Pp6efQ_ghiA',
            user_id=user.id
        )

    def test_bio(self):
        profile = Profile.objects.get(bio='test bio')
        self.assertEqual(profile.bio, 'test bio')        