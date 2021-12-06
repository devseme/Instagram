from django import forms
from django.db.models import fields
from insta.models import Images,Profile,Likes,Comment

class UserForm(forms.ModelForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={

        'id': 'imageform', 'class': 'uploadimage'

    }))

    class Meta:
        model = Images
        fields = ['image','name','caption','liked']
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')        