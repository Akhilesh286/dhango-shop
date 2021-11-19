# Generated by Django 3.2.9 on 2021-11-19 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('owner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('star', models.FloatField()),
                ('image', models.CharField(max_length=2555)),
                ('discription', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('stock', models.FloatField()),
                ('video', models.CharField(max_length=2555)),
                ('discount', models.FloatField()),
                ('image2', models.CharField(max_length=2555)),
                ('image3', models.CharField(max_length=2555)),
                ('image4', models.CharField(max_length=2555)),
                ('image5', models.CharField(max_length=2555)),
            ],
        ),
    ]
