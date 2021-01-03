from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
@stringfilter
def blogContentFilter(value, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    result = '<p class="blog_content">%s</p>' % esc(value).replace('\n','</p><p class="blog_content">')
    return mark_safe(result)
#[EOF]