# Generated by Django 5.0.2 on 2024-04-01 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column1', models.CharField(max_length=200)),
                ('column2', models.CharField(max_length=200)),
                ('column3', models.CharField(max_length=200)),
            ],
        ),
    ]
