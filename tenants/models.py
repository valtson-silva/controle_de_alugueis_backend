from django.db import models

# Cria o modelo Tenants
class Tenants(models.Model):
    name = models.CharField(max_length=255, null=False)
    contact = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=255, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    date_update = models.DateTimeField(auto_now=True)
