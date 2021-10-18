# Generated by Django 3.2.8 on 2021-10-18 18:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('foodboard', '0004_alter_ingredientusage_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='CookEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='cook date')),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foodboard.recipe')),
            ],
        ),
    ]
