# Generated by Django 5.0.1 on 2024-01-24 18:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0008_driverprofile_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=100)),
                ('day', models.DateField(blank=True)),
                ('booked', models.DateTimeField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.customer')),
                ('driver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='one.driver')),
            ],
        ),
    ]
