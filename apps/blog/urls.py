from django.urls import path

from .views import CategoryViewSet, BlogListView, BlogItemView, Blog_Create
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = router.urls

urlpatterns += [
    path('blog/', BlogListView.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogItemView.as_view(), name='blog_item'),
    path('create/', Blog_Create.as_view(), name = 'create_blog')
]
