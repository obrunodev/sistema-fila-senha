# Generated by Django 4.2.16 on 2024-09-22 06:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('departments', '0005_queue_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='queue',
            name='called',
        ),
    ]
