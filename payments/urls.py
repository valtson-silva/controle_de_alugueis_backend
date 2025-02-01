from django.urls import path
from .views import (
    PaymentsCreateView, PaymentsDeleteView, PaymentsDetailView, PayoutsReportView,
    PaymentsListViews, PaymentsTenantsListView, PaymentsUpdateView
)

# Endpoints
urlpatterns = [
    path('create/', PaymentsCreateView.as_view(), name='payment_create'),
    path('', PaymentsListViews.as_view(), name='payments_get'),
    path('<int:id>/', PaymentsDetailView.as_view(), name='payment_get'),
    path('<int:tenant_id>/tenants/', PaymentsTenantsListView.as_view(), name='payments_tenants_get'),
    path('<int:id>/update/', PaymentsUpdateView.as_view(), name='payment_update'),
    path('<int:id>/delete/', PaymentsDeleteView.as_view(), name='payment_delete'),
    path('report/', PayoutsReportView.as_view(), name='payouts_report_get')
]