from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter

from blog.apis import PostViewSet
from blog.views import IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthorView, LinkListView
from typeidea.custom_site import custom_site

router = DefaultRouter()
router.register(r'post', PostViewSet, basename='api_post')


urlpatterns = [
    path('super_admin/', admin.site.urls),
    path('admin/', custom_site.urls),
    path('', IndexView.as_view(), name='post_list_all'),
    path('category/<int:category_id>/', CategoryView.as_view(), name='post_list_category'),
    path('tag/<int:tag_id>/', TagView.as_view(), name='post_list_tag'),
    path('post/<int:post_id>.html', PostDetailView.as_view(), name='post_detail'),
    path('links/', LinkListView.as_view(), name='links'),
    path('search/', SearchView.as_view(), name='search'),
    path('author/<int:author_id>/', AuthorView.as_view(), name='author'),

    path('api/', include(router.urls)),
    # path('swagger-ui/', TemplateView.as_view(
    #     template_name='swagger-ui.html',
    #     extra_context={'schema_url': 'openapi-schema'}
    # ), name='swagger-ui'),
]
