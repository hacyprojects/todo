# Generated by Django 5.0.2 on 2024-02-21 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='2023-02-15'),
            preserve_default=False,
        ),
    ]