from django.shortcuts import render
from Blog.models import *
# Create your views here.
def BlogIndex(request):
    blog_post = Blogs.objects.all()
    numOf_post = Blogs.objects.count()
    blog_category = BlogCategory.objects.all()
    params = {'blog_post': blog_post , 'blog_category': blog_category, 'numOf_post': numOf_post}
    return render(request, 'Blog/blog-index.html', params)


def BlogDetail(request, BlogSlug):
    blog_posts = Blogs.objects.get(slug = BlogSlug)
    blog_category = BlogCategory.objects.all().order_by('-id')[:4]
    params = {'blog_posts': blog_posts, 'blog_category':blog_category}
    return render(request, 'Blog/blog-details.html', params)