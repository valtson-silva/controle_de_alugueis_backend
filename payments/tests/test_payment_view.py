import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tenants.models import Tenants
from payments.models import Payments
from django.utils.timezone import now
from datetime import timedelta

def create_tenant():
    return Tenants.objects.create(
        name="João da Silva",
        email="joao@email.com",
        contact="999999999"
    )

@pytest.mark.django_db
def test_payout_list():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    url = reverse('payments_get')
    client.login(username="testuser", password="testpass")
    
    response = client.get(url)
    
    assert response.status_code == 200 
    
    
@pytest.mark.django_db
def test_create_payment():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    url = reverse("payment_create")
    
    client.login(username="testuser", password="testpass")
    tenant = create_tenant()
    
    response = client.post(url, {
        "value": 1000.00,
        "tenant": tenant.id,
        "due_date": "2025-01-30",
        },
        format='json')
    
    assert response.status_code == 201
    
    
@pytest.mark.django_db
def test_report_payments():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    client.login(username="testuser", password="testpass")
    
    tenant = create_tenant()
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
    
    url = reverse("payouts_report_get")
    
    response = client.get(url)
    
    # Verifica se as informações estão corretas
    assert response.data["pagos"][0]["status"] == "pago"
    assert response.data["pendentes"][0]["status"] == 'pendente'
    assert response.data["atrasados"][0]["status"] == "atrasado"
    