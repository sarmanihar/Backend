# Generated by Django 4.0.5 on 2022-06-22 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('united_world', '0002_email_send_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email_send',
            name='body',
            field=models.TextField(),
        ),
    ]
