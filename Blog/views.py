from django.shortcuts import render
from.models import *
# Create your views here.

def BlogIndex(request):
    posts = Blogs.objects.all()
    context = {'posts':posts}
    return render(request,'Blog/blog.html', context)


def BlogDetails(request, blogslug):
    posts = Blogs.objects.get(slug = blogslug)
    context = {'posts': posts}
    return render(request, 'Blog/blog-details.html', context)