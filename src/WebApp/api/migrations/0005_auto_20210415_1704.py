# Generated by Django 3.1.7 on 2021-04-15 23:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210415_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='developer',
            old_name='headQuaters',
            new_name='headQuarters',
        ),
    ]
