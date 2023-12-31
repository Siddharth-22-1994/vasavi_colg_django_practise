# Generated by Django 5.0 on 2023-12-18 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='pics')),
                ('upload', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='std1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('place', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
