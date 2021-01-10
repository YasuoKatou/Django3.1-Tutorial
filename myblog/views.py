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

#[EOF]