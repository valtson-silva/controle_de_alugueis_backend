# Generated by Django 5.1.5 on 2025-01-29 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('due_date', models.DateField()),
                ('status', models.CharField(choices=[('pago', 'Pago'), ('atrasado', 'Atrasado')], default='pendente', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tenants.tenants')),
            ],
        ),
    ]
