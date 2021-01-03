from django.db import models
from django.utils import timezone

# Create your models here.

class BlogContent(models.Model):
    content_title = models.CharField(max_length=128)
    content_text  = models.TextField(max_length=4096)
    create_date   = models.DateTimeField(default=timezone.now)
    update_date   = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.content_title

class BlogTag(models.Model):
    tag_text      = models.CharField(max_length=128)

    def __str__(self):
        return self.tag_text

class BlogTagList(models.Model):
    blog_content  = models.ForeignKey(BlogContent, on_delete=models.CASCADE)
    blog_tag      = models.ForeignKey(BlogTag, on_delete=models.CASCADE)

    def __str__(self):
        return self.blog_tag.tag_text + ' : ' + self.blog_content.content_title
#[EOF]