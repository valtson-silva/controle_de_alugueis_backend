from rest_framework import serializers
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    email = serializers.CharField(required=True)
    
    class Meta:
        # Define o modelo
        model = User
        # Define os campos
        fields = ['username', 'password', 'email']
        
    def validate_email(self, value):
        # Verifica se o email já existe
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Este E-mail já está em uso.")
        return value
        
    def create(self, validated_data):
        # Cria o usuário com a senha criptografada
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data.get('email', '')
        )
        return user