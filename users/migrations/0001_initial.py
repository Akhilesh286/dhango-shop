# Generated by Django 3.2.9 on 2021-12-02 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=100)),
                ('phone', models.IntegerField()),
                ('date', models.DateField()),
                ('gender', models.CharField(max_length=50)),
            ],
        ),
    ]
