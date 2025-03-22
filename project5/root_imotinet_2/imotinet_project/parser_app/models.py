from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self):
        return self.url
    
class Advertisement(models.Model):
    url = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self):
        return self.url

class Pages(models.Model):
    url = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self):
        return self.url
    
class Agent(models.Model):
    agency_photo = models.CharField(max_length=500, null=True, blank=True)
    agency_name = models.CharField(max_length=500, null=True, blank=True)
    agency_email = models.CharField(max_length=500, null=True, blank=True)
    agency_phone = models.CharField(max_length=500, null=True, blank=True)
    agency_adress = models.CharField(max_length=500, null=True, blank=True)
    agency_contact_link = models.CharField(max_length=500, null=True, blank=True)
    agency_contact_link_2 = models.CharField(max_length=500, null=True, blank=True)
    
    agent_name = models.CharField(max_length=500, null=True, blank=True)
    agent_photo = models.CharField(max_length=500, null=True, blank=True)
    agent_phone = models.CharField(max_length=500, unique=True)
    agent_adress = models.CharField(max_length=500, null=True, blank=True)
    is_trusted = models.BooleanField(default=False)
    
    def __str__(self):
        return self.agent_name