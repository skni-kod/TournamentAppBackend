# Generated by Django 3.1.7 on 2021-04-07 14:40

import datetime
import django.core.validators
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_auto_20210407_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='memberslimit',
            field=models.IntegerField(blank=True, default=5, validators=[django.core.validators.MinValueValidator(2)]),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tournament',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 4, 7, 16, 40, 17, 132025), validators=[django.core.validators.MinValueValidator(datetime.datetime(2021, 4, 7, 14, 40, 17, 132024, tzinfo=utc))]),
        ),
    ]
