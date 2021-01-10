from django.contrib import admin

from .models import BlogContent, BlogTag
# Register your models here.

admin.site.register(BlogContent)
admin.site.register(BlogTag)

#[EOF]