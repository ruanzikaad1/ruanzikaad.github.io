# Generated by Django 4.2.5 on 2023-10-20 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0028_balance_value_affiliate'),
    ]

    operations = [
        migrations.CreateModel(
            name='smsFunnel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('external_id', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'smsFunnel',
                'managed': True,
            },
        ),
    ]