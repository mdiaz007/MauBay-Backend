# Generated by Django 5.1.6 on 2025-02-26 00:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='category',
            field=models.CharField(choices=[('Cars', 'Cars'), ('Jewelry', 'Jewelry'), ('Clothing', 'Clothing')], max_length=50),
        ),
    ]
