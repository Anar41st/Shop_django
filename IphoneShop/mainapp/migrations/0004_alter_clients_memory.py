# Generated by Django 4.2.7 on 2024-01-09 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_alter_clients_empl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='memory',
            field=models.IntegerField(blank=True, null=True, verbose_name='Память'),
        ),
    ]
