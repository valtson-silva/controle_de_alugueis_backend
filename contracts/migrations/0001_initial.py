# Generated by Django 5.1.5 on 2025-01-29 01:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('properties', '0001_initial'),
        ('tenants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('properties', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='properties.properties')),
                ('tenants', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='tenants.tenants')),
            ],
        ),
    ]
