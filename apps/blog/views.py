from drf_util.decorators import serialize_decorator
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.blog.serializers import BlogAllSerializer
from .models import Category, Blog, Comments
from .serializers import CategorySerializer, BlogSerializer, CommentsSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blogs = Blog.objects.all()
        return Response(BlogSerializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        blog = get_object_or_404(Blog.objects.filter(pk=pk))
        response_data = BlogSerializer(blog).data
        return Response(response_data)


class BlogCreate(GenericAPIView):
    serializer_class = BlogSerializer

    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(BlogSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        blog = Blog.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
            body=validated_data['body'],
            category=validated_data['category'],
        )

        blog.save()

        return Response(BlogSerializer(blog).data)


class CommentsCreate(GenericAPIView):
    serializer_class = CommentsSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CommentsSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        comments = Comments.objects.create(
            comments_text=validated_data['comments_text'],
            comments_blog=validated_data['comments_blog'],
        )
        comments.save()
        return Response(CommentsSerializer(comments).data)
