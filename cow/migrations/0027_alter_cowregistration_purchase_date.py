# Generated by Django 4.0.8 on 2023-11-02 08:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cow', '0026_alter_sick_cow_cow_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cowregistration',
            name='purchase_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
