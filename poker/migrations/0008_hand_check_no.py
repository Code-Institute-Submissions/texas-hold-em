# Generated by Django 2.0.8 on 2018-12-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0007_hand_player_bet'),
    ]

    operations = [
        migrations.AddField(
            model_name='hand',
            name='check_no',
            field=models.IntegerField(default=0),
        ),
    ]