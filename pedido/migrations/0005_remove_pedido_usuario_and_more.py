# Generated by Django 4.2.6 on 2024-05-22 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pedido', '0004_pedidoprato_desconto_unitario_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='usuario',
        ),
        migrations.RemoveField(
            model_name='pedidoprato',
            name='desconto_unitario',
        ),
        migrations.RemoveField(
            model_name='pedidoprato',
            name='preco_unitario',
        ),
    ]
