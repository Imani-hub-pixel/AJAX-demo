from django.urls import include,path
from . import views

urlpatterns=[
    path('',views.index,name='index'),
    path('like_post/',views.like_post,name='like_post'),
]
