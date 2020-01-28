# Generated by Django 3.0.2 on 2020-01-27 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='type',
            field=models.IntegerField(choices=[(1, 'Hospital'), (2, 'Vendor'), (3, 'User'), (4, 'Admin')], default=3, verbose_name='type'),
        ),
    ]
