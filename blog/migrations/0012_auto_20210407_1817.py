# Generated by Django 3.1.4 on 2021-04-07 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20210407_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='slug',
            field=models.SlugField(max_length=200, primary_key=True, serialize=False, unique=True),
        ),
    ]
