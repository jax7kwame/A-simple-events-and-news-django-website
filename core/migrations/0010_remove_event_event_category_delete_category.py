# Generated by Django 5.0.1 on 2024-01-10 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_newspost_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='event_category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]