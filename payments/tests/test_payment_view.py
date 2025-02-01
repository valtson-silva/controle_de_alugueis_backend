import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tenants.models import Tenants
from payments.models import Payments
from django.utils.timezone import now
from datetime import timedelta

# Testa o método get para obter todos os pagamentos
@pytest.mark.django_db
def test_payout_list():
    # Simula um cliente HTTP
    client = APIClient()
    # Registra um usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")
    # Obtém a url
    url = reverse('payments_get')
    # Faz o login 
    client.login(username="testuser", password="testpass")
    # Faz a requisição get
    response = client.get(url)
    
    # Verifica se o status retornado foi 200 OK
    assert response.status_code == 200 
    
# Testa o método post para criar um pagamento
@pytest.mark.django_db
def test_create_payment():
    # Simula um cliente HTTP
    client = APIClient()
    # Registra um usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")
    # Gera a url
    url = reverse("payment_create")
    # Faz o login 
    client.login(username="testuser", password="testpass")
    
    # Cria um inquilino
    tenant = Tenants.objects.create(
        name="João da Silva",
        email="joao@email.com",
        contact="999999999"
    )
    
    # Faz a requisição post para criar um pagamento
    response = client.post(url, {
        "value": 1000.00,
        "tenant": tenant.id,
        "due_date": "2025-01-30",
        },
        format='json')
    
    # Verifica se o status retornado foi 201 Created
    assert response.status_code == 201
    
@pytest.mark.django_db
def test_report_payments():
    # Simula um cliente HTTP
    client = APIClient()
    # Cria um usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")
    # Faz o login
    client.login(username="testuser", password="testpass")
    # Cria um inquilino
    tenant = Tenants.objects.create(
        name="João da Silva",
        email="joao@email.com",
        contact="999999999"
    )
    # Cria 3 pagamentos
    Payments.objects.create(
        value=1000,
        tenant=tenant,
        due_date=now().date() + timedelta(days=2)
    )
    Payments.objects.create(
        value=1000,
        tenant=tenant,
        due_date=now().date() + timedelta(days=2),
        status="pago"
    )
    Payments.objects.create(
        value=1000,
        tenant=tenant,
        due_date=now().date() - timedelta(days=2),
        status="atrasado"
    )
    # Obtém a url
    url = reverse("payouts_report_get")
    # Faz a requisição get
    response = client.get(url)
    
    # Verifica se as informações estão corretas
    assert response.data["pagos"][0]["status"] == "pago"
    assert response.data["pendentes"][0]["status"] == 'pendente'
    assert response.data["atrasados"][0]["status"] == "atrasado"