from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password', 'is_superuser', 'date_joined', 'last_login', 'is_staff', 'email', 'is_active')


class UserActivateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('is_active',)
        

class UserRegistrSerializer(serializers.ModelSerializer):
    # Поле для повторения пароля
    # password2 = serializers.CharField()
    
    # Настройка полей
    class Meta:
        # Поля модели которые будем использовать
        model = User
        # Назначаем поля которые будем использовать
        fields = ['email', 'password']
        # fields = '__all__'
 
    # Метод для сохранения нового пользователя
    def save(self, *args, **kwargs):
        # Создаём объект класса User
        user = User(
            email = self.validated_data['email'], # Назначаем Email
            username = self.validated_data['email'], # Назначаем Логин
            is_active = True
        )
        # Проверяем на валидность пароль
        password = self.validated_data['password']
        # Сохраняем пароль
        user.set_password(password)
        # Сохраняем пользователя
        user.save()
        # Возвращаем нового пользователя 
        return user
