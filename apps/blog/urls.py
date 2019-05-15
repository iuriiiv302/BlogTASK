from django.urls import path

from apps.blog.views import BlogUpdate, ComentsUbdate, BlogTrue, BlogDelete
from .views import CategoryViewSet, BlogListView, BlogItemView, BlogCreate, CommentsCreate, CategoryCreate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('create_blog/', BlogCreate.as_view(), name = 'create_blog'),
    path('create_comment/',CommentsCreate.as_view(), name= 'create_comments'),
    path('update_blog/',BlogUpdate.as_view(), name= 'update_blog'),
    path('update_commit/', ComentsUbdate.as_view(), name= 'update_commit'),
    path('create_category/', CategoryCreate.as_view(), name = 'create_category'),
    path('blog_true/', BlogTrue.as_view(), name = 'show_blog_true'),
    path('blog_delete/<int:pk>/', BlogDelete.as_view(), name = 'blog_delete'),
]
