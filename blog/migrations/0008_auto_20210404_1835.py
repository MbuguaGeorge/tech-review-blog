# Generated by Django 3.1.4 on 2021-04-04 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210404_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trend',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
