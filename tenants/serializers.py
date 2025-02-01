from rest_framework import serializers
from .models import Tenants

class TenantsSerializer(serializers.ModelSerializer):
    class Meta:
        # Define o modelo
        model = Tenants
        # Define os campos
        fields = ['id', 'name', 'contact', 'email', 'created_at', 'date_update']