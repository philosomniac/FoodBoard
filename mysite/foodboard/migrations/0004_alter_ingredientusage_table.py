# Generated by Django 3.2.8 on 2021-10-15 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodboard', '0003_alter_ingredientusage_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='ingredientusage',
            table='foodboard_ingredient_usage',
        ),
    ]