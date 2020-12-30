from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.http.response import JsonResponse
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

def edit_blog_content(request):
    blog = BlogContent(id=int(request.POST['myblog-id']),
      content_title=request.POST['content_title'],
      content_text=request.POST['content_text'])
    blog.save()

    return HttpResponseRedirect('/myblog/')

def get_blog_by_id(request):
    dic = QueryDict(request.body, encoding='utf-8')
    # print(dic.get('myblog_id'))
    rec = BlogContent.objects.get(id=int(dic.get('myblog_id')))
    json = {
      "myblog_id": rec.id,
      "content_title": rec.content_title,
      "content_text": rec.content_text,
      "update_date": rec.update_date
    }
    return JsonResponse(json)
#[EOF]