from rest_framework import serializers
from .models import Tenants

class TenantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenants
        fields = ['id', 'name', 'contact', 'email', 'created_at', 'date_update']