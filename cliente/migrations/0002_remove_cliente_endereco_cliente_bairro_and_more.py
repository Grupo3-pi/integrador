# Generated by Django 4.2.6 on 2024-05-22 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='endereco',
        ),
        migrations.AddField(
            model_name='cliente',
            name='bairro',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='cidade',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='numero',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='cliente',
            name='rua',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]