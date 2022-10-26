# Generated by Django 4.0.5 on 2022-10-01 17:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('R1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj', models.CharField(max_length=100)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('user', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='signup',
            name='city',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='country',
            field=models.CharField(default=5, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='signup',
            name='state',
            field=models.CharField(default=6, max_length=50),
            preserve_default=False,
        ),
    ]
