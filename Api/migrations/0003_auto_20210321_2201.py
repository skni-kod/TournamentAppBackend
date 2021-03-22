# Generated by Django 3.1.7 on 2021-03-21 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_tournament'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournament',
            name='time',
            field=models.TimeField(blank=True, default='12:00'),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='maxcategory',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='mincategory',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='tournament',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
