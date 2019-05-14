from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "password",)


class UserInfoSerializers(serializers.ModelSerializer):

    def get_id(self, obj):
        id = User.objects.filter(id=obj.id)
        return UserSerializer(id).data

    class Meta:
        model = User
        fields = ('username', 'email')
