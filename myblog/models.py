from django.db import models

# Create your models here.

class BlogContent(models.Model):
    content_title = models.CharField(max_length=128)
    content_text  = models.TextField(max_length=4096)
    create_date   = models.DateTimeField()
    update_date   = models.DateTimeField()

class BlogTag(models.Model):
    tag_text      = models.CharField(max_length=128)
