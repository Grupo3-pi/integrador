# Generated by Django 4.2 on 2023-05-14 23:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio', '0002_prato_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='prato',
            name='foto',
            field=models.ImageField(default='image.jpeg', upload_to='static/media'),
        ),
    ]