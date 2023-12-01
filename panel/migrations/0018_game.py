# Generated by Django 4.2.5 on 2023-10-11 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('panel', '0017_profile_bet_game_profile_in_game'),
    ]

    operations = [
        migrations.CreateModel(
            name='game',
            fields=[
                ('id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('hash_game', models.CharField(max_length=255)),
                ('bet', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('payout', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('is_win', models.BooleanField(default=False)),
                ('is_finished', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
