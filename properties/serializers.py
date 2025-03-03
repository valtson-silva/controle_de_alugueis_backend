from rest_framework import serializers
from .models import Properties

class PropertiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Properties
        fields = ['id', 'address', 'type', 'rent', 'status', 'created_at', 'date_update']