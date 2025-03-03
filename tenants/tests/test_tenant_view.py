import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.mark.django_db
def test_tenants_list():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    url = reverse('tenants_get')
    client.login(username="testuser", password="testpass")
    
    response = client.get(url)
    
    assert response.status_code == 200
    
@pytest.mark.django_db
def test_create_tenant():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    url = reverse('tenant_create')
    client.login(username="testuser", password="testpass")
    
    response = client.post(url, {
        "name": "João da Silva",
        "contact": "99999999",
        "email": "joao@email.com",
    })
    
    assert response.status_code == 201
