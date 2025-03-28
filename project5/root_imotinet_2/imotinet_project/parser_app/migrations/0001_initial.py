# Generated by Django 5.1.2 on 2024-10-29 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500, unique=True)),
                ('status', models.CharField(default='New', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agency_photo', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_name', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_email', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_phone', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_adress', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_contact_link', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_contact_link_2', models.CharField(blank=True, max_length=500, null=True)),
                ('agent_name', models.CharField(blank=True, max_length=500, null=True)),
                ('agent_photo', models.CharField(blank=True, max_length=500, null=True)),
                ('agent_phone', models.CharField(max_length=500, unique=True)),
                ('agent_adress', models.CharField(blank=True, max_length=500, null=True)),
                ('is_trusted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('url', models.CharField(max_length=500)),
                ('status', models.CharField(default='New', max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=500, unique=True)),
                ('status', models.CharField(default='New', max_length=500)),
            ],
        ),
    ]
