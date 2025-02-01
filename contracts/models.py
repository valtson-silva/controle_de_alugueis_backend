from django.db import models
from properties.models import Properties
from tenants.models import Tenants

# Cria o modelo Contracts
class Contracts(models.Model):
    start_date = models.DateField(null=False)
    end_date = models.DateField(null=False)
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    properties = models.ForeignKey(Properties, on_delete=models.RESTRICT, null=False)
    tenants = models.ForeignKey(Tenants, on_delete=models.RESTRICT, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)