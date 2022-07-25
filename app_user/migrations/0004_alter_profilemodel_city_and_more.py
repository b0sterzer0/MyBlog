# Generated by Django 4.0.3 on 2022-07-12 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_user', '0003_remove_profilemodel_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='city',
            field=models.CharField(default=None, max_length=40, null=True, verbose_name='city'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='date_of_birth',
            field=models.DateField(default=None, null=True, verbose_name='date of birth'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='hobby',
            field=models.TextField(default=None, null=True, verbose_name='hobby'),
        ),
    ]