# Generated by Django 5.1.2 on 2024-10-31 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agent',
            name='agency_link',
        ),
    ]
