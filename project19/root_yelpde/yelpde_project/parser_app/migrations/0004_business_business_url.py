# Generated by Django 5.1.2 on 2024-11-12 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0003_search'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='business_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
