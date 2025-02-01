from rest_framework import serializers
from .models import Contracts

class ContractsSerializer(serializers.ModelSerializer):
    class Meta:
        # Define o modelo
        model = Contracts
        # Define os campos
        fields = ['id', 'start_date', 'end_date', 'value', 'properties', 'tenants', 'created_at', 'date_update']
        
        
    def validate(self, data):
        # Validação personalizada para garantir que start_date < end_date
        if data['start_date'] >= data['end_date']:
            raise serializers.ValidationError("A data de início deve ser anterior à data de término.")
        return data