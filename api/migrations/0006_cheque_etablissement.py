# Generated by Django 5.0.2 on 2024-06-24 19:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_etat_etablissement'),
    ]

    operations = [
        migrations.AddField(
            model_name='cheque',
            name='etablissement',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='cheque_etablissement', to='api.etablissement'),
        ),
    ]