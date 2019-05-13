from django.urls import path

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
    # path('comment/detail/',CommentsDetail.as_view(), name= 'views_comments'),


]
