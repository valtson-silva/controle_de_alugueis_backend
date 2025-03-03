from rest_framework import serializers
from .models import Contracts

class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contracts
        fields = ['id', 'start_date', 'end_date', 'value', 'properties', 'tenants', 'created_at', 'date_update']
        
        
    def validate(self, data):
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("A data de início deve ser anterior à data de término.")
        return data