# Generated by Django 5.1.3 on 2024-11-11 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_usuario_edad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='edad',
            field=models.IntegerField(),
        ),
    ]
