# Generated by Django 3.2 on 2021-10-23 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentist', '0005_auto_20211022_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='duration',
            field=models.IntegerField(verbose_name='Xizmat davomiyligi'),
        ),
    ]
