# Generated by Django 5.1.2 on 2024-11-07 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_app', '0005_alter_agency_facets_buy_alter_agency_facets_rent_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='facets_rent',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='agency',
            name='facets_sold',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
