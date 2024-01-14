# Generated by Django 5.0.1 on 2024-01-07 17:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_category_delete_newspostcomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('-category_title',), 'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='event',
            name='event_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='core.category'),
            preserve_default=False,
        ),
    ]
