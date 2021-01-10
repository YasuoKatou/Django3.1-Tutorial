from django.db import models
from django.utils import timezone

# Create your models here.

class BlogTag(models.Model):
    tag_text      = models.CharField(max_length=128)

    def __str__(self):
        return self.tag_text

class BlogContent(models.Model):
    content_title = models.CharField(max_length=128)
    content_text  = models.TextField(max_length=4096)
    create_date   = models.DateTimeField(default=timezone.now)
    update_date   = models.DateTimeField(default=timezone.now)

    blog_tags     = models.ManyToManyField(BlogTag, null=True, blank=True)

    def __str__(self):
        return "[Title]" + self.content_title

#[EOF]