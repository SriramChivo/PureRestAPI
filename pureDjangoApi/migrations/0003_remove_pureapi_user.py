# Generated by Django 2.1.5 on 2020-06-30 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pureDjangoApi', '0002_auto_20200628_2154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pureapi',
            name='user',
        ),
    ]
