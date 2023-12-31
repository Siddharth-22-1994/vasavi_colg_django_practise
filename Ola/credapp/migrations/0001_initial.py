# Generated by Django 5.0 on 2023-12-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_name', models.CharField(max_length=30)),
                ('E_id', models.CharField(max_length=20, unique=True)),
                ('E_email', models.EmailField(max_length=254)),
                ('E_salary', models.FloatField(default=0.0)),
            ],
        ),
    ]
