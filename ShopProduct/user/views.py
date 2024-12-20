from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView
from shopproduct.tasks import send_welcome_email  # Импорт задачи
from shopproduct.user.serializers import UserRegistrationSerializer, UserBaseSerializer


@extend_schema(
    request=UserBaseSerializer,  # Описываем, какой сериалайзер используется для входящих данных (запрос)
    responses={200: UserBaseSerializer, 201: UserBaseSerializer},  # Описываем, какой сериалайзер используется для ответа
)
class UserInfoView(APIView):
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]

    def get(self, request):
        # Получаем всех пользователей
        users = User.objects.all()

        # Формируем список данных о пользователях
        user_data = [
            {
                "username": user.username,
                "email": user.email,
                # Можно добавить любые другие поля, которые вам нужны
            }
            for user in users
        ]
        # Возвращаем список пользователей в виде JSON
        return Response(user_data, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def perform_create(self, serializer):
        # Создаём пользователя
        user = serializer.save()
        # Отправляем задачу для приветственного письма
        send_welcome_email.delay(user.email, user.username)
