# Generated by Django 5.1.2 on 2024-11-05 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent_id', models.IntegerField(unique=True)),
                ('agent_uuid', models.CharField(blank=True, max_length=500, null=True)),
                ('user_uuid', models.CharField(blank=True, max_length=500, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
                ('first_name', models.CharField(blank=True, max_length=500, null=True)),
                ('last_name', models.CharField(blank=True, max_length=500, null=True)),
                ('avatar_uuid', models.CharField(blank=True, max_length=500, null=True)),
                ('avatar_name', models.CharField(blank=True, max_length=500, null=True)),
                ('avatar_ext', models.CharField(blank=True, max_length=500, null=True)),
                ('position', models.CharField(blank=True, max_length=500, null=True)),
                ('occupation_id', models.IntegerField(blank=True, null=True)),
                ('occupation_title', models.CharField(blank=True, max_length=500, null=True)),
                ('primary_specialization_id', models.IntegerField(blank=True, null=True)),
                ('primary_specialization_title', models.CharField(blank=True, max_length=500, null=True)),
                ('specializations', models.CharField(blank=True, max_length=500, null=True)),
                ('email', models.CharField(blank=True, max_length=500, null=True)),
                ('phones', models.CharField(blank=True, max_length=500, null=True)),
                ('work_regions', models.CharField(blank=True, max_length=500, null=True)),
                ('deleted', models.IntegerField(blank=True, null=True)),
                ('confirmed', models.IntegerField(blank=True, null=True)),
                ('updated_at', models.CharField(blank=True, max_length=500, null=True)),
                ('sorting', models.IntegerField(blank=True, null=True)),
                ('views_count', models.IntegerField(blank=True, null=True)),
                ('is_avatar', models.BooleanField(blank=True, null=True)),
                ('agency_uuid', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_title', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_logo_uuid', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_logo_name', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_logo_ext', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_slug', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_obdn_uuid', models.CharField(blank=True, max_length=500, null=True)),
                ('agency_obdn_title', models.CharField(blank=True, max_length=500, null=True)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('reviews_count', models.IntegerField(blank=True, null=True)),
                ('promote', models.IntegerField(blank=True, null=True)),
                ('type_name', models.CharField(blank=True, max_length=500, null=True)),
                ('json_data', models.JSONField(blank=True, null=True)),
                ('status', models.CharField(default='New', max_length=500)),
            ],
        ),
    ]
