# Generated by Django 5.1.6 on 2025-03-22 03:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_maubay_users_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maubay_users',
            name='seller',
        ),
    ]
