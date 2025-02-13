import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_properties_list():
    # Simula um cliente HTTP
    client = APIClient()
    # Registra um usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")
    
    url = reverse('properties_get')
    
    client.login(username="testuser", password="testpass")
    
    response = client.get(url)
    
    # Verifica se o status retornado foi 200 OK
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_create_tenant():
     
    client = APIClient()
    
    user = User.objects.create_user(username="testuser", password="testpass")
    
    url = reverse('property_create')
    
    client.login(username="testuser", password="testpass")
    
    response = client.post(url, {
        "address": "Rua A",
        "type": "casa",
        "rent": 100.00,
        "status": "disponível"
    })
    
    # Verifica se o status retornado foi 201 created
    assert response.status_code == 201
