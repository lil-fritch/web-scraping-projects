# Generated by Django 5.1.2 on 2024-11-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0017_business_history'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='json_data_description',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
