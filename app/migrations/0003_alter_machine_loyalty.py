# Generated by Django 3.2.9 on 2021-12-17 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211217_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='machine',
            name='loyalty',
            field=models.BooleanField(default=False),
        ),
    ]