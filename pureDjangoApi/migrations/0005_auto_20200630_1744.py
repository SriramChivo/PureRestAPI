# Generated by Django 2.1.5 on 2020-06-30 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pureDjangoApi', '0004_auto_20200630_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pureapi',
            name='Address',
            field=models.CharField(max_length=60),
        ),
    ]
