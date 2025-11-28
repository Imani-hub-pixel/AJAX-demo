from django.shortcuts import render
from django.http import HttpResponse
from.models import Post, Like


# Create your views here.
def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})

def like_post(request):
    if request.method=='POST':
        post_id=request.GET['post_id']
        liked_post=Post.objects.get(pk=post_id)
        Like.objects.create(post=liked_post)
        return HttpResponse('Liked')
    return HttpResponse('Invalid request')