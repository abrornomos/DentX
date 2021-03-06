# Generated by Django 3.2 on 2021-09-02 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('illness', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='aids',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='anesthesia',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='asthma',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='diabet',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='dizziness',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='hepatitis',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tavsif'),
        ),
        migrations.AddField(
            model_name='pressure',
            name='desc',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Tavsif'),
        ),
    ]
