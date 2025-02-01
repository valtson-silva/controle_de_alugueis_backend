from django.db import models
from tenants.models import Tenants

# Cria o modelo Payments
class Payments(models.Model):
    value = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    due_date = models.DateField(null=False)
    status = models.CharField(max_length=100, choices=[('pago', 'Pago'), ('atrasado', 'Atrasado')], default="pendente")
    tenant = models.ForeignKey(Tenants, on_delete=models.RESTRICT, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)