# Generated by Django 4.0.4 on 2022-06-13 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('electronic_service', '0003_remove_client_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='firm_NIP_REGON',
        ),
        migrations.RemoveField(
            model_name='client',
            name='firm_name',
        ),
    ]
