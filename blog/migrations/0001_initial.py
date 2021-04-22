# Generated by Django 3.1.4 on 2021-04-22 18:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=100)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('confirmed', models.BooleanField(default=False)),
                ('confirmation_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Trend',
            fields=[
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('category', models.CharField(choices=[('Programming', 'Programming'), ('Cryptocurrency', 'Cryptocurrency'), ('Blockchain', 'Blockchain'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things', 'Internet of Things'), ('Machine Learning', 'Machine Learning')], default='Cryptocurrency', max_length=50)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('title', models.CharField(max_length=200, unique=True)),
                ('slug', models.SlugField(max_length=255, primary_key=True, serialize=False, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', tinymce.models.HTMLField(verbose_name='content')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('category', models.CharField(choices=[('Programming', 'Programming'), ('Cryptocurrency', 'Cryptocurrency'), ('Blockchain', 'Blockchain'), ('Artificial Intelligence', 'Artificial Intelligence'), ('Internet of Things', 'Internet of Things'), ('Machine Learning', 'Machine Learning')], default='Programming', max_length=50)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
