# Generated by Django 4.0.3 on 2022-07-12 10:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='add_date',
            field=models.DateField(default=datetime.date(2022, 7, 12), verbose_name='add date'),
        ),
    ]
