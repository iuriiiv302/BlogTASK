# Create your views here.
from django.contrib.auth.models import User
from drf_util.decorators import serialize_decorator
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from apps.users.serializers import UserSerializer, UserInfoSerializers


class RegisterUserView(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(UserSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data

        user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            is_superuser=True,
            is_staff=True
        )
        user.set_password(validated_data['password'])
        user.save()

        return Response(UserSerializer(user).data)


class InfoUser(GenericAPIView):
    serializer_class = UserInfoSerializers
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request, pk):
        user = get_object_or_404(User.objects.filter(pk=pk))
        response_data = UserInfoSerializers(user).data
        return Response(response_data)


class CreateUser(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    @serialize_decorator(UserSerializer)
    def post(self, request):
        validated_data = request.serializer.validated_data
        new_user = User.objects.create(
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            username=validated_data['username'],
            password=validated_data['password'],
        )

        new_user.save()
        return Response(UserSerializer(new_user).data)

class TrueUser(GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = (AllowAny,)
    authentication_classes = ()

    def get(self, request):
        user_true = User.objects.filter(is_superuser=True)
        return Response(UserSerializer(user_true, many=True).data)