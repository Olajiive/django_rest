# Generated by Django 4.0 on 2023-08-18 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drfapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='occupation',
            field=models.CharField(default='new string', max_length=100),
        ),
    ]