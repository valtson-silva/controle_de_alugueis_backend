from rest_framework import serializers
from .models import Properties

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        # Define o modelo
        model = Properties
        # Define os campos
        fields = ['id', 'address', 'type', 'rent', 'status', 'created_at', 'date_update']