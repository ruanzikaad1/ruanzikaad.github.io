# Generated by Django 4.2.5 on 2023-10-16 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0023_alter_deposits_qr_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cpf',
            field=models.CharField(max_length=16),
        ),
    ]