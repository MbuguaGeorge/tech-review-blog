# Generated by Django 3.1.4 on 2021-04-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
