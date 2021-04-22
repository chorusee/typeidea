from django.urls import path, re_path

from blog import views1

urlpatterns = [
    re_path(r'^$', views1.post_list, name='post_list_all'),
    path('category/<int:category_id>', views1.post_list, name='post_list_category'),
    path('tag/<int:tag_id>', views1.post_list, name='post_list_tag'),
    path('post/<int:post_id>.html', views1.post_detail, name='post_detail'),
    path('links/', views1.links, name='links'),
]
