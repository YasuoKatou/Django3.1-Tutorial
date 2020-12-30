from django.urls import path

from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new_blog_content/', views.new_blog_content, name='new_blog_content'),
    path('edit_blog_content/', views.edit_blog_content, name='edit_blog_content'),
    path('get_blog_by_id/', views.get_blog_by_id, name='get_blog_by_id'),
]
