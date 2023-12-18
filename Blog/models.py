from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
from django.db.models.signals import pre_save
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField



# Create your models here.

class Author(models.Model):
    Name = models.CharField(max_length = 50, default = "", blank = False)
    Profile = models.ImageField(default="", upload_to="Blog Author/")
    slug = models.SlugField(max_length = 500, null = True, blank = True, unique = True)

    def __str__(self) -> str:
        return self.Name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Name)
        super(Author, self).save(*args, **kwargs)



class Category(models.Model):
    Title = models.CharField(max_length=100, default="")
    Icon = models.CharField(default="", max_length=100)
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)

    def __str__(self):
        return self.Title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.Title)
        super(Category, self).save(*args, **kwargs)


class Blogs(models.Model):
    UserId = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Author = models.ForeignKey(Author, on_delete=models.CASCADE, default="")
    Category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    Title = models.CharField(max_length=500, default="")
    Description = RichTextUploadingField()
    Cover = models.ImageField(upload_to='Blog Cover', default="", null=True)
    slug = models.SlugField(max_length=500, null=True, blank=True, unique=True)
    created_at = models.DateTimeField(default=timezone.now, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return self.Title
    


def create_slug(instance, new_slug=None):
    slug = slugify(instance.Title)
    if new_slug is not None:
        slug = new_slug
    qs = Blogs.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)


pre_save.connect(pre_save_post_reciever, Blogs)



class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
