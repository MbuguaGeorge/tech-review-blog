# Generated by Django 3.1.4 on 2021-04-12 14:47

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20210410_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='content',
            field=tinymce.models.HTMLField(verbose_name='content'),
        ),
    ]