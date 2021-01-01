from django.http import HttpResponse, HttpResponseRedirect, QueryDict
from django.http.response import JsonResponse
from django.views import generic

from .models import BlogContent, BlogTag
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

def get_tag_list(request):
  '''
  タグの一覧を取得する
  '''
  list = []
  for rec in BlogTag.objects.order_by('tag_text'):
    list.append({"id": rec.id, "name": rec.tag_text})
  return JsonResponse({"list": list})

def add_tag_list(request):
  '''
  タグを追加する
  '''
  dic = QueryDict(request.body, encoding='utf-8')
  blog = BlogTag(tag_text=dic.get('tag_text'))
  blog.save()

  # タグの一覧を返す
  return get_tag_list(request)
#[EOF]