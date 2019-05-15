from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Category, Blog, Comments


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


# ----------------------------------------------------------------------------------------------

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['comments_text', 'comments_blog']


class CommentsUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    def validate_id(self, value):
        comment = Comments.objects.filter(id=value).first()
        if not comment:
            raise ValidationError("Not exists")
        return value

    class Meta:
        model = Comments
        fields = ['id', "comments_text"]


# --------------------------------------------------------------------------------------------------
class BlogSerializer(serializers.ModelSerializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = Comments.objects.filter(comments_blog_id=obj.id)
        return CommentsSerializer(comments, many=True).data

    class Meta:
        model = Blog
        fields = ['title', 'slug', 'body', 'posted', 'category', 'enabled', "comments"]


class BlogUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    def validate_id(self, value):
        post = Blog.objects.filter(id=value).first()
        if not post:
            raise ValidationError("Not exists")
        return value

    class Meta:
        model = Blog
        fields = ['id', 'title', 'body', 'slug', 'category', 'enabled']

#
# class BlogIdSerializer(serializers.ModelSerializer):
#     def validate_id(self, value):
#         post = Blog.objects.filter(id=value).first()
#         if not post:
#             raise ValidationError("Not exists")
#         return value
#
#     class Meta:
#         model = Blog
#         fields = ['title', 'slug', 'body', 'posted', 'category', 'enabled']
