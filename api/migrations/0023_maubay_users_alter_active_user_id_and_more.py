# Generated by Django 5.1.6 on 2025-03-18 02:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0022_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='maubay_users',
            fields=[
                ('user_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('firstname', models.TextField(max_length=50)),
                ('lastname', models.TextField(max_length=50)),
                ('username', models.TextField(max_length=50)),
                ('account_created', models.DateField(auto_now=True)),
                ('seller', models.BooleanField(default=False)),
            ],
        ),
        migrations.AlterField(
            model_name='active',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='deleted',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='draft',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='sold',
            name='user_id',
            field=models.CharField(max_length=100),
        ),
    ]
