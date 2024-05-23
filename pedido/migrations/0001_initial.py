# Generated by Django 4.2.6 on 2024-05-19 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cardapio', '0005_prato_valor'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_pedido', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('P', 'Pendente'), ('E', 'Em Preparo'), ('F', 'Finalizado'), ('C', 'Cancelado')], default='P', max_length=1)),
                ('valor_total', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('desconto', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cliente.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='PedidoPrato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantidade', models.PositiveIntegerField()),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pedido.pedido')),
                ('prato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cardapio.prato')),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='pratos',
            field=models.ManyToManyField(through='pedido.PedidoPrato', to='cardapio.prato'),
        ),
    ]