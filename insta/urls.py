from django.urls import path
from . import views

urlpatterns=[
    # url('^$',views.welcome,name = 'welcome'),
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('like/', views.like_image, name='like-image'),
    path('search/', views.search_post, name='search.post'),
    path('comment/', views.post_detail, name='post_detail')
]
