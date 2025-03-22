from django.db import models

class Agency(models.Model):
    url = models.CharField(max_length=500, unique=True)
    office_fax = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(default="New")
    
    def __str__(self):
        return self.url
    
class Agent(models.Model):
    agent_name = models.CharField(unique=True)
    agent_license = models.CharField(max_length=500, blank=True, null=True)
    agent_url = models.CharField(max_length=500, blank=True, null=True)
    agent_photo = models.CharField(max_length=500, blank=True, null=True)
    agency_name = models.CharField(max_length=500, blank=True, null=True)
    agency_office_phone = models.CharField(max_length=500, blank=True, null=True)
    agency_office_fax = models.CharField(max_length=500, blank=True, null=True)
    agency_address = models.CharField(max_length=500, blank=True, null=True)
    agency_photo = models.CharField(max_length=500, blank=True, null=True)
    agency_url = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.agent_name