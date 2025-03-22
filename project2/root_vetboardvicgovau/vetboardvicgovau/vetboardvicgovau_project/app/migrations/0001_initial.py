# Generated by Django 5.1.2 on 2024-10-25 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=500, null=True)),
                ('status', models.CharField(blank=True, max_length=500, null=True)),
                ('registration_no', models.CharField(blank=True, max_length=500, null=True)),
                ('endorsed_in', models.CharField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
