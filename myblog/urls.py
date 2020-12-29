from django.urls import path

from . import views

app_name = 'myblog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('new_blog_content/', views.new_blog_content, name='new_blog_content'),
]
