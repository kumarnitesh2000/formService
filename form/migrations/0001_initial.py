# Generated by Django 2.1.4 on 2020-08-25 00:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Form', max_length=30)),
                ('description', models.TextField(default='Description Section', max_length=250)),
                ('publishDate', models.DateTimeField()),
                ('endValidity', models.DateTimeField()),
                ('slug', models.SlugField(unique_for_date='publishDate')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Untitled Form', max_length=30)),
                ('description', models.TextField(default='Description Section', max_length=250)),
                ('form', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Form')),
            ],
        ),
    ]