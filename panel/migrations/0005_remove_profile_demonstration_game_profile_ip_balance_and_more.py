# Generated by Django 4.2.5 on 2023-10-10 19:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel', '0004_alter_profile_demonstration_game'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='demonstration_game',
        ),
        migrations.AddField(
            model_name='profile',
            name='ip',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='balance',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('fake_value', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('permited_withdraw', models.BooleanField(default=True)),
                ('only_fake', models.BooleanField(default=False)),
                ('balance_created_at', models.DateTimeField(auto_now_add=True)),
                ('balance_updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'balance',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='affiliate',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
                ('total_earnings', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cpa_percent', models.DecimalField(decimal_places=2, default=10.0, max_digits=10)),
                ('cpa_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('revshare', models.DecimalField(decimal_places=2, default=30.0, max_digits=10)),
                ('revshare_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('affiliate_created_at', models.DateTimeField(auto_now_add=True)),
                ('affiliate_updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'affiliate',
                'managed': True,
            },
        ),
    ]