# Generated by Django 4.0.3 on 2022-07-12 10:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0002_profilemodel_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profilemodel',
            name='name',
        ),
    ]
