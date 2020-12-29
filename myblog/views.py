from django.http import HttpResponseRedirect
from django.views import generic

from .models import BlogContent
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'myblog/index.html'
    context_object_name = 'myblog_content_list'

    def get_queryset(self):
        return BlogContent.objects.order_by('-create_date')

def new_blog_content(request):
    blog = BlogContent(content_title=request.POST['content_title'],
      content_text=request.POST['content_text'])
    blog.save()

    return HttpResponseRedirect('/myblog/')
#[EOF]