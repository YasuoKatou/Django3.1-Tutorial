from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def blogContentFilter(value, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<p class="blog_content">%s</p>' % esc(value.content_text).replace('\n','</p><p class="blog_content">')
    if hasattr(value, 'blog_tags'):
        result += '<ul class="myblog-tags">'
        for tag in value.blog_tags.all():
            result += "<li>%s</li>" % tag.tag_text
        result += "</ul>"

    return mark_safe(result)
#[EOF]