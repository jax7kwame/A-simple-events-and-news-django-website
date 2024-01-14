# Generated by Django 5.0.1 on 2024-01-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_remove_event_event_category_delete_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='event_photo',
            field=models.ImageField(blank=True, upload_to='uploads/events'),
        ),
        migrations.AlterField(
            model_name='event',
            name='speaker_image',
            field=models.ImageField(blank=True, upload_to='uploads/speakers'),
        ),
        migrations.AlterField(
            model_name='event',
            name='sponsor_logo',
            field=models.ImageField(blank=True, upload_to='uploads/logos'),
        ),
        migrations.AlterField(
            model_name='newspost',
            name='image',
            field=models.ImageField(blank=True, upload_to='uploads/news'),
        ),
    ]