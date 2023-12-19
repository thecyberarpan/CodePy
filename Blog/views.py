from django.shortcuts import render, redirect
from Blog.models import *
from .forms import BlogSearchForm
from django.http import JsonResponse


# Create your views here.
def BlogIndex(request):
    blog_post = Blogs.objects.all()
    selected_category = request.GET.get('category', None)
    if selected_category and selected_category != 'All Categories':
        blog_post = Blogs.objects.filter(Category__Title=selected_category)
    else:
        blog_post = Blogs.objects.all()

    numOf_post = Blogs.objects.count()
    blog_category = BlogCategory.objects.all()
    search_form = BlogSearchForm(request.GET)

    # Check if the form is valid
    if search_form.is_valid():
        search_query = search_form.cleaned_data['search_query']
        # Filter posts based on the search query
        blog_post = blog_post.filter(Title__icontains=search_query)

    params = {'blog_post': blog_post , 'blog_category': blog_category, 'numOf_post': numOf_post, 'selected_category': selected_category, 'search_form': search_form}
    return render(request, 'Blog/blog-index.html', params)




def BlogDetail(request, BlogSlug):
    blog_posts = Blogs.objects.get(slug=BlogSlug)
    blog_category = BlogCategory.objects.all().order_by('-id')[:4]
    params = {'blog_posts': blog_posts, 'blog_category': blog_category}
    return render(request, 'Blog/blog-details.html', params)
