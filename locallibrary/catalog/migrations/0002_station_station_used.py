# Generated by Django 2.2.2 on 2020-07-13 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='station_used',
            field=models.BooleanField(default=False),
        ),
    ]