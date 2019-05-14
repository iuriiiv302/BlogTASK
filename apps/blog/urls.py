from django.urls import path

from apps.blog.views import BlogUpdate
from .views import CategoryViewSet, BlogListView, BlogItemView, BlogCreate, CommentsCreate
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('create/', BlogCreate.as_view(), name = 'create_blog'),
    path('comment/',CommentsCreate.as_view(), name= 'create_comments'),
    path('update_blog/',BlogUpdate.as_view(), name= 'update_blog'),

]
