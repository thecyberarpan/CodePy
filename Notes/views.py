from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
# Create your views here.


def Index(request):
    notes = Notes.objects.all()
    category = Category.objects.all()[:4]
    author = Author.objects.all()
    context = {'notes': notes, 'category': category, 'author': author}
    return render(request, 'Notes/index.html', context)


def GetNotes(request):
    notes = Notes.objects.all()
    category = Category.objects.all()
    context = {'notes': notes, 'category': category}
    return render(request, 'Notes/note-list.html', context)


def NotesDetails(request, slug):
    notes = Notes.objects.get(slug=slug)
    category = Category.objects.all()
    context = {'notes': notes, 'category': category, 'authslug': notes.Author.slug}
    return render(request, 'Notes/note-details.html', context)


def AllCategory(request):
    category = Category.objects.all().order_by('-id')
    context = {'category': category}
    return render(request, 'Notes/category-list.html', context)


def CategoryDetails(request, catslug):
    category = Category.objects.get(slug=catslug)
    notes = Notes.objects.filter(Category=category).order_by('-id')
    context = {'category': category, 'notes': notes}
    return render(request, 'Notes/category-details.html', context)


def AllAuthor(request):
    author = Author.objects.all()
    context = {'author': author}
    return render(request, 'Notes/instructors-list.html', context)


def AuthorDetails(request, authslug):
    author = Author.objects.get(slug=authslug)
    author_posts = Notes.objects.filter(Author=author)
    context = {'author': author, 'author_posts': author_posts}
    return render(request, 'Notes/instructors-single.html', context)


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