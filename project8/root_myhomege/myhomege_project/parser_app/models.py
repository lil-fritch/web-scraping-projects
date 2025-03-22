from django.db import models

class Agent(models.Model):
    agent_id = models.CharField(max_length=500)
    full_name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    st_count = models.IntegerField(null=True, blank=True)
    
    agency_id = models.CharField(max_length=500, null=True, blank=True)
    agency_name = models.CharField(max_length=500, null=True, blank=True)
    agency_phones = models.CharField(max_length=500, null=True, blank=True)
    agency_email = models.CharField(max_length=500, null=True, blank=True)
    agency_logo = models.CharField(max_length=500, null=True, blank=True)
    agency_banner = models.CharField(max_length=500, null=True, blank=True)
    agency_type_id = models.CharField(max_length=500, null=True, blank=True)
    agency_creator_id = models.CharField(max_length=500, null=True, blank=True)
    has_logo = models.CharField(max_length=500, null=True, blank=True)
    logo_ver = models.CharField(max_length=500, null=True, blank=True)
    agency_st_count = models.CharField(max_length=500, null=True, blank=True)
    address_geo = models.CharField(max_length=500, null=True, blank=True)
    address_eng = models.CharField(max_length=500, null=True, blank=True)
    address_ru = models.CharField(max_length=500, null=True, blank=True)
    
    agent_json = models.JSONField()
    agency_json = models.JSONField()
    status = models.CharField(default='New', max_length=4)
    
    def __str__(self):
        return str(self.agent_id)