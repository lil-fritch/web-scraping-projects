# Generated by Django 5.1.2 on 2024-11-16 12:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0015_business_description_2_business_history_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='business',
            name='history',
        ),
    ]
