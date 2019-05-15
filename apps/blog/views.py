from drf_util.decorators import serialize_decorator
from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Category, Blog, Comments
from apps.blog.serializers import BlogUpdateSerializer, CommentsUpdateSerializer, CategorySerializer, BlogSerializer, \
    CommentsSerializer


# CATEGORY__________________________________________________________________

class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class CategoryCreate(GenericAPIView):
    serializer_class = CategorySerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(CategorySerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        category = Category.objects.create(
            title=validated_data['title'],
            slug=validated_data['slug'],
        )

        category.save()

        return Response(CategorySerializer(category).data)


# BLOG_________________________________________________________________
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


class BlogUpdate(GenericAPIView):
    serializer_class = BlogUpdateSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def put(self, request):
        serializer = BlogUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            blog = Blog.objects.get(id=data['id'])
            blog.title = data["title"]
            blog.body = data["body"]
            blog.slug = data["slug"]
            blog.category = data["category"]
            blog.enabled = data["enabled"]
            blog.save()
            response_data = BlogSerializer(blog).data
            return Response(response_data)
        else:
            return Response(serializer.errors, status=400)


class BlogTrue(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        blog_true = Blog.objects.filter(enabled=True)
        return Response(BlogSerializer(blog_true, many=True).data)


class BlogDelete(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def delete(self, request, pk):
        Blog.objects.get(pk=pk).delete()
        return Response({"status": "delete", "id": pk})

# COMMENTS________________________________________________________________________________

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


class ComentsUbdate(GenericAPIView):
    serializer_class = CommentsUpdateSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def put(self, request):
        serializer = CommentsUpdateSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            comment = Comments.objects.get(id=data['id'])
            comment.comments_text = data["comments_text"]
            comment.save()
            response_data = CommentsSerializer(comment).data
            return Response(response_data)
        else:
            return Response(serializer.errors, status=400)
