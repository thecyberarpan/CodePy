from django.contrib import admin
from.models import *
# Register your models here.
admin.site.register(BlogCategory)
admin.site.register(BlogAuthor)
admin.site.register(Blogs)



# admin.py


class Blogs(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'created_at', 'updated_at')

    class Media:
        js = ('ckeditor/ckeditor.js', 'ckeditor/ckeditor-init.js',)