# Generated by Django 2.1.3 on 2018-12-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='NumeroDocumento',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]