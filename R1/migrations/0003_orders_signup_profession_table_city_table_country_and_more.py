# Generated by Django 4.0.5 on 2022-10-07 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('R1', '0002_table_signup_city_signup_country_signup_state'),
    ]

    operations = [
        migrations.CreateModel(
            name='orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buye', models.CharField(max_length=100)),
                ('order', models.CharField(max_length=100)),
                ('p', models.CharField(max_length=100)),
                ('dorn', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='signup',
            name='profession',
            field=models.CharField(default=2, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='city',
            field=models.CharField(default=3, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='country',
            field=models.CharField(default=4, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='off',
            field=models.CharField(default=6, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='price',
            field=models.CharField(default=9, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='table',
            name='state',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
    ]