from rest_framework.generics import CreateAPIView
from users.serializers import UserSerializer
from users.models import User
from rest_framework.permissions import AllowAny


class UserCreateAPIView(CreateAPIView):
    """
    Создание нового пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        """Создаём нового пользователя, и хешируем ему пароль"""

        user = serializer.save()
        user.set_password(user.password)
        user.save()
