# Generated by Django 4.1.5 on 2023-01-13 02:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 13, 2, 13, 57, 323081, tzinfo=datetime.timezone.utc)),
        ),
    ]
