# Generated by Django 5.1.2 on 2024-10-29 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0004_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='facebook',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='instagram',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='linkedin',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='youtube',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
