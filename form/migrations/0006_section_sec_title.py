# Generated by Django 2.1.4 on 2020-08-25 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0005_remove_section_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='sec_title',
            field=models.CharField(default='Untitled Section', max_length=30),
        ),
    ]
