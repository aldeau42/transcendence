# Generated by Django 5.0.6 on 2024-09-04 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0005_player_email_2fa_active_player_sms_2fa_active_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='qr_2fa_active',
            field=models.BooleanField(default=False),
        ),
    ]