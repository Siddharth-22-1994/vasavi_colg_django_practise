# Generated by Django 5.0 on 2023-12-16 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stud',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
