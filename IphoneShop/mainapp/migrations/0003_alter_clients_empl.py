# Generated by Django 4.2.7 on 2024-01-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_alter_clients_memory_alter_clients_numb_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='empl',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='ФИО сотрудника'),
        ),
    ]
