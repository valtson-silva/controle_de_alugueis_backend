from rest_framework import serializers
from .models import Payments

class PaymentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payments
        fields = ['id', 'value', 'status', 'tenant', 'due_date', 'created_at', 'date_update']