# Generated by Django 4.0.5 on 2022-08-03 16:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('united_world', '0007_remove_room_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='ans',
        ),
    ]
