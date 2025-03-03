import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tenants.models import Tenants
from properties.models import Properties
from contracts.models import Contracts

def create_tenant():
    return Tenants.objects.create(
        name="João da Silva",
        email="joao@email.com",
        contact="999999999"
    )
    
def create_estate():
    return Properties.objects.create(
        address="Rua B",
        type="casa",
        rent=1000.00,
        status="disponível"
    )

def create_contract():
    tenant = create_tenant()
    estate = create_estate()
    
    return Contracts.objects.create(
        start_date ="2025-03-10",
        end_date="2026-01-10",
        value= 1000,
        tenants=tenant,
        properties=estate
    )

@pytest.mark.django_db
def test_contracts_list():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    url = reverse('contracts_get')
    client.login(username="testuser", password="testpass")

    response = client.get(url)
    
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_contract():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    url = reverse('contract_create')
    
    client.login(username="testuser", password="testpass")
    
    tenant = create_tenant()
    estate = create_estate()

    response = client.post(url, {
        "start_date": "2025-03-10",
        "end_date": "2026-01-10",
        "value": 1000,
        "tenants": tenant.id,
        "properties": estate.id
    })
    
    assert response.status_code == 201
    
@pytest.mark.django_db
def test_property_tenant_contract():
    client = APIClient()
    user = User.objects.create_user(username="testuser", password="testpass")
    contract = create_contract()
    
    url = reverse('properties_tenants_contracts_get', args=[contract.properties.id, contract.tenants.id])
    client.login(username="testuser", password="testpass")
    response = client.get(url)

    # Verifica se o contrato obtido possui as informações corretas
    assert response.status_code == 200
    assert response.data[0]['tenants'] == contract.tenants.id
    assert response.data[0]['properties'] == contract.properties.id
