from django.urls import path
from .views import (
    ContractsCreateView, ContractsDeleteView, ContractsDetailView,
    ContractsListView, ContractsPropertiesTenantsListView, ContractsUpdateView
)

# Endpoints
urlpatterns = [
    path('', ContractsListView.as_view(), name='contracts_get'),
    path('create/', ContractsCreateView.as_view(), name='contract_create'),
    path('<int:id>/', ContractsDetailView.as_view(), name='contract_get'),
    path('properties/<int:properties_id>/tenants/<int:tenants_id>/', ContractsPropertiesTenantsListView.as_view(), name='properties_tenants_contracts_get'),
    path('<int:id>/update/', ContractsUpdateView.as_view(), name='contract_update'),
    path('<int:id>/delete/', ContractsDeleteView.as_view(), name='contract_delete')
]