from django.urls import path
from .views import (
    TenantsCreateView, TenantsDeleteView, TenantsDetailView,
    TenantsListView, TenantsUpdateView
)

urlpatterns = [
    path('', TenantsListView.as_view(), name='tenants_get'),
    path('create/', TenantsCreateView.as_view(), name='tenant_create'),
    path('<int:id>/', TenantsDetailView.as_view(), name='tenant_get'),
    path('<int:id>/update/', TenantsUpdateView.as_view(), name='tenant_update'),
    path('<int:id>/delete/', TenantsDeleteView.as_view(), name='tenant_delete')
    
]