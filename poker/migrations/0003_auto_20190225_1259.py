# Generated by Django 2.0.8 on 2019-02-25 12:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poker', '0002_table_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='owner',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
