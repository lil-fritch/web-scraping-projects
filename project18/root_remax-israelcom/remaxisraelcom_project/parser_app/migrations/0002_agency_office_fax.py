# Generated by Django 5.1.2 on 2024-11-08 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='office_fax',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
