import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

# Testa o login do usuário
@pytest.mark.django_db
def test_login_user():
    # Cria um usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")
    
    url = reverse('login')
    # Simula um cliente HTTP
    client = APIClient()
    # Faz a requisição post
    response = client.post(url, {"username": "testuser", "password": "testpass"}, format="multipart")
    
    # Verifica se o login foi feito com sucesso
    assert response.status_code == 200
    assert "sessionid" in response.cookies
