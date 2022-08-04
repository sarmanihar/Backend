# Generated by Django 4.0.5 on 2022-08-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('united_world', '0004_message_room'),
    ]

    operations = [
        migrations.DeleteModel(
            name='email_send',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
        migrations.RemoveField(
            model_name='room',
            name='name',
        ),
        migrations.AddField(
            model_name='room',
            name='Answer1',
            field=models.CharField(default=5, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='Answer2',
            field=models.CharField(default=7, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='Answer3',
            field=models.CharField(default=9, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='Answer4',
            field=models.CharField(default=3, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='Options',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='Question',
            field=models.CharField(default=5, max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='room',
            name='S_Answer',
            field=models.CharField(default=4, max_length=15),
            preserve_default=False,
        ),
    ]
