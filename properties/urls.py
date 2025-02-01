from django.urls import path
from .views import (
    PropertiesCreateView, PropertiesDeleteView, PropertiesDetailView, 
    PropertiesListView, PropertiesUpdateView
)

# Endpoints
urlpatterns = [
    path('', PropertiesListView.as_view(), name='properties_get'),
    path('<int:id>/', PropertiesDetailView.as_view(), name='property_get'),
    path('create/', PropertiesCreateView.as_view(), name='property_create'),
    path('<int:id>/update/', PropertiesUpdateView.as_view(), name='property_update'),
    path('<int:id>/delete/', PropertiesDeleteView.as_view(), name='property_delete')
]