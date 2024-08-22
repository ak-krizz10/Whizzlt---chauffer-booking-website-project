# Generated by Django 5.0.1 on 2024-01-19 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Driverprofile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('place', models.CharField(max_length=100)),
                ('license', models.CharField(blank=True, max_length=30)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('exp', models.IntegerField(blank=True)),
                ('availability', models.BooleanField(default=False)),
                ('picture', models.ImageField(blank=True, default='avatar_driver.jpg', upload_to='Driver')),
            ],
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
    ]
