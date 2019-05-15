from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password", "email", "is_superuser")


class UserInfoSerializers(serializers.ModelSerializer):

    def get_id(self, obj):
        id = User.objects.filter(id=obj.id)
        return UserSerializer(id).data

    class Meta:
        model = User
        fields = ('username', 'email')


class UserUpdateSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField()

    def validate_id(self, value):
        post = User.objects.filter(id=value).first()
        if not post:
            raise ValidationError("Not exists")
        return value

    class Meta:
        model = User
        fields = ('id', 'username', 'email')
