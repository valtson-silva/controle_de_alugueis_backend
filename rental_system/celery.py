from celery import Celery
import os

# Define as configurações padrão do Django para o Celery
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rental_system.settings")

app = Celery("rental_system")

# Carrega as configurações do Celery do settings.py
app.config_from_object("django.conf:settings", namespace="CELERY")

# Descobre automaticamente tasks nas APIs registradas
app.autodiscover_tasks()
