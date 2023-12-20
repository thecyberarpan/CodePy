from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.decorators import login_required
from Blog.models import Blogs
from .forms import SubscriberForm
from .models import Subscriber
from django.contrib import messages


# Create your views here.

def Index(request):
    notes = Notes.objects.all()
    blog_posts = Blogs.objects.all().order_by('-id')[:6]
    category = Category.objects.all()[:4]
    author = Author.objects.all()

    if request.method == "POST":
        subscribe_email = request.POST.get('CallToAcrtion')
        #check if email already exists
        if Subscriber.objects.filter(email = subscribe_email).exists():
            messages.error(request, "This email is already subscribed")
        else:
            # Create an instance of your Subscriber model
            subscriber_instance = Subscriber(email=subscribe_email)
            
            # Save the instance to the database
            subscriber_instance.save()

    context = {'notes': notes, 'category': category, 'author': author, 'blog_posts':  blog_posts}
    return render(request, 'Notes/index.html', context)


@login_required(login_url="/account/login")
def GetNotes(request):
    notes = Notes.objects.all()
    category = Category.objects.all()
    context = {'notes': notes, 'category': category}
    return render(request, 'Notes/note-list.html', context)


@login_required(login_url="/account/login")
def NotesDetails(request, slug):
    notes = Notes.objects.get(slug=slug)
    category = Category.objects.all()
    context = {'notes': notes, 'category': category, 'authslug': notes.Author.slug}
    return render(request, 'Notes/note-details.html', context)


@login_required(login_url="/account/login")
def AllCategory(request):
    category = Category.objects.all().order_by('-id')
    context = {'category': category}
    return render(request, 'Notes/category-list.html', context)


@login_required(login_url="/account/login")
def CategoryDetails(request, catslug):
    category = Category.objects.get(slug=catslug)
    notes = Notes.objects.filter(Category=category).order_by('-id')
    context = {'category': category, 'notes': notes}
    return render(request, 'Notes/category-details.html', context)


@login_required(login_url="/account/login")
def AllAuthor(request):
    author = Author.objects.all()
    context = {'author': author}
    return render(request, 'Notes/instructors-list.html', context)


@login_required(login_url="/account/login")
def AuthorDetails(request, authslug):
    author = Author.objects.get(slug=authslug)
    author_posts = Notes.objects.filter(Author=author)
    context = {'author': author, 'author_posts': author_posts}
    return render(request, 'Notes/instructors-single.html', context)


@login_required(login_url="/account/login")
def filtered_results(request):
    # Get selected category IDs from the request's GET parameters
    category_ids = request.GET.getlist('categories')

    # If no categories are selected, show all posts
    if not category_ids:
        notes = Notes.objects.all()
    else:
        # Filter posts based on selected categories
        notes = Notes.objects.filter(Category__id__in=category_ids)

    # Retrieve all categories for display
    category = Category.objects.all()

    context = {'notes': notes, 'category': category}
    return render(request, 'Notes/filtered-results.html', context)


def error_404_view(request, exception):
    return render(request, 'Notes/404.html')