# Generated by Django 4.2.5 on 2023-10-10 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('panel', '0007_remove_profile_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='affiliate',
            name='personalized_code',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]