# Generated by Django 5.0.1 on 2024-01-19 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0005_customer_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='customer',
            field=models.SlugField(blank=True, max_length=100, null=True),
        ),
    ]
