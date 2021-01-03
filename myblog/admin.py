from django.contrib import admin

from .models import BlogContent, BlogTag, BlogTagList
# Register your models here.

admin.site.register(BlogContent)
admin.site.register(BlogTag)
admin.site.register(BlogTagList)

#[EOF]