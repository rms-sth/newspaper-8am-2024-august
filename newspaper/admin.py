from django.contrib import admin

from newspaper.models import Category, Post, Tag

admin.site.register(Post)
admin.site.register(Category)
admin.site.register(Tag)
