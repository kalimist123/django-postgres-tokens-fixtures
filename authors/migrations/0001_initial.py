from __future__ import unicode_literals
from django.db import migrations, models
from django.contrib.auth.models import User  # where User lives
import os


def forwards_func(apps, schema_editor):
    # build the user you now have access to via Django magic
    User.objects.create_superuser('mick', 'johnny@someemail.com', '#superpassword!')


def reverse_func(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400)),
                ('publisher', models.CharField(max_length=400)),
                ('release_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('biography', models.TextField()),
                ('date_of_birth', models.DateField()),
                ('books', models.ManyToManyField(blank=True, related_name='authors', to='authors.Book')),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('genre', models.TextField()),
                ('date_of_release', models.DateField()),
            ],
        ),
        migrations.RunPython(forwards_func, reverse_func),
    ]
