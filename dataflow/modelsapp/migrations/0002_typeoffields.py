# Generated by Django 5.0 on 2023-12-16 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='typeoffields',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('average', models.DecimalField(decimal_places=2, max_digits=6)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('date_time', models.DateTimeField(default=datetime.datetime(2023, 12, 16, 12, 7, 54, 350219))),
                ('email', models.EmailField(max_length=254)),
                ('feedback', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('weblinks', models.URLField(max_length=250)),
                ('Ip', models.GenericIPAddressField()),
                ('salary', models.FloatField()),
            ],
        ),
    ]
