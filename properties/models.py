from django.db import models

# Cria o modelo Properties
class Properties(models.Model):
    address = models.CharField(max_length=255, null=False)
    type = models.CharField(max_length=100, choices=[('casa', 'Casa'), ('apartamento', 'Apartamento')], null=False)
    rent = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    status = models.CharField(max_length=100, choices=[('disponível', 'Disponível'), ('alugado', 'Alugado')], null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)