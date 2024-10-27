from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from tutorial.quickstart.serializers import UserSerializer

from ShopProduct.user.serializers import UserRegistrationSerializer


@extend_schema(
    request=UserSerializer,  # Описываем, какой сериалайзер используется для входящих данных (запрос)
    responses={200: UserSerializer, 201: UserSerializer}  # Описываем, какой сериалайзер используется для ответа
)
class UserInfoView(APIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]  # Только авторизованные пользователи могут видеть информацию


    def get(self, request):
        user = request.user
        # Возвращаем данные, относящиеся к пользователю
        return Response({
            "username": user.username,
            "email": user.email,
            # Любая другая информация о пользователе
        })


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated] # Разрешаем всем доступ к регистрации
    serializer_class = UserRegistrationSerializer
