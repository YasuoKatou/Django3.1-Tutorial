from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

import markdown

register = template.Library()

@register.filter
@stringfilter
def blogContentFilter(value, autoescape=True):
    if autoescape:
        esc = conditional_escape
    else:
        esc = lambda x: x
    md = markdown.Markdown()
    html = md.convert(value)
    #result = '<p class="blog_content">%s</p>' % esc(value).replace('\n','</p><p class="blog_content">')
    result = html

    return mark_safe(result)

@register.filter
def blogTags(value, autoescape=True):
    result = ""
    if hasattr(value, 'blog_tags'):
        result += '<ul class="myblog-tags">'
        for tag in value.blog_tags.all():
            result += "<li>%s</li>" % tag.tag_text
        result += "</ul>"

    return mark_safe(result)
#[EOF]