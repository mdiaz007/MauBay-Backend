# Generated by Django 5.1.6 on 2025-02-26 00:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_items_category'),
    ]

    operations = [
        migrations.DeleteModel(
            name='items',
        ),
    ]
