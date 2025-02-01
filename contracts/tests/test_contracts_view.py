import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from tenants.models import Tenants
from properties.models import Properties
from contracts.models import Contracts

@pytest.mark.django_db
def test_contracts_list():
    # Simula um cliente HTTP
    client = APIClient()
    # Cria um usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")
    # Obtém a url
    url = reverse('contracts_get')
    # Faz o login
    client.login(username="testuser", password="testpass")
    # Faz a requisição get
    response = client.get(url)
    
    # Verifica se o status retornado foi 200 OK
    assert response.status_code == 200

@pytest.mark.django_db
def test_create_contract():
    # Simula um cliente HTTP
    client = APIClient()
    # Cria um usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")
    # Obtém a url
    url = reverse('contract_create')
    # Faz o login
    client.login(username="testuser", password="testpass")
    # Cria um inquilino de teste
    tenant = Tenants.objects.create(
        name="João da Silva",
        email="joao@email.com",
        contact="999999999"
    )
    # Cria uma propriedade de teste
    estate = Properties.objects.create(
        address="Rua B",
        type="casa",
        rent=1000.00,
        status="disponível"
    )
    # Faz a requisição post
    response = client.post(url, {
        "start_date": "2025-03-10",
        "end_date": "2026-01-10",
        "value": 1000,
        "tenants": tenant.id,
        "properties": estate.id
    })
    
    # Verifica se o status retornado foi 201 created
    assert response.status_code == 201
    
@pytest.mark.django_db
def test_property_tenant_contract():
     # Simula um cliente HTTP
    client = APIClient()
    # Cria um usuário de teste
    user = User.objects.create_user(username="testuser", password="testpass")
    # Cria um inquilino de teste
    tenant = Tenants.objects.create(
        name="João da Silva",
        email="joao@email.com",
        contact="999999999"
    )
    # Cria uma propriedade de teste
    estate = Properties.objects.create(
        address="Rua B",
        type="casa",
        rent=1000.00,
        status="disponível"
    )
    # Cria um contrato de teste
    contract = Contracts.objects.create(
        start_date ="2025-03-10",
        end_date="2026-01-10",
        value= 1000,
        tenants=tenant,
        properties=estate
    )
    # Obtém a url
    url = reverse('properties_tenants_contracts_get', args=[estate.id, tenant.id])
    # Faz o login
    client.login(username="testuser", password="testpass")
    # Faz a requisição get
    response = client.get(url)

    # Verifica se o contrato obtido possui as informações corretas
    assert response.status_code == 200
    assert response.data[0]['tenants'] == tenant.id
    assert response.data[0]['properties'] == estate.id
