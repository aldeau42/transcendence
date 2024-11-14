# Generated by Django 5.0.6 on 2024-09-07 07:59

import player.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0011_remove_player_is_profile_picture_player_lose_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='player',
            name='connected',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='player',
            name='profile_picture',
            field=models.ImageField(blank=True, default='fallback.jpg', null=True, upload_to=player.models.upload_to_profile_pictures),
        ),
    ]