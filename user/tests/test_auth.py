import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from django.urls import reverse

@pytest.mark.django_db
def test_login_user():
    user = User.objects.create_user(username="testuser", password="testpass")
    url = reverse('login')
    client = APIClient()
    response = client.post(url, {"username": "testuser", "password": "testpass"}, format="multipart")
    
    assert response.status_code == 200
    assert "sessionid" in response.cookies
