from django.contrib import admin

from newspaper.models import (
    Category,
    Post,
    Tag,
    UserProfile,
    Comment,
    Contact,
    Newsletter,
)
from django_summernote.admin import SummernoteModelAdmin

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(UserProfile)
admin.site.register(Comment)
admin.site.register(Contact)
admin.site.register(Newsletter)


class PostAdmin(SummernoteModelAdmin):
    summernote_fields = ("content",)


admin.site.register(Post, PostAdmin)
