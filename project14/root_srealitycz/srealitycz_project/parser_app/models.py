from django.db import models

class Agency(models.Model):
    url = models.CharField(unique=True, max_length=500)
    status = models.CharField(max_length=500, default="New")
    
    def __str__(self):
        return self.url
    
class Agent(models.Model):
    agent_id = models.IntegerField(unique=True)
    ico = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=500, null=True, blank=True)
    phones = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    image = models.CharField(max_length=500, null=True, blank=True)
    rating = models.CharField(max_length=500, null=True, blank=True)
    review_count = models.CharField(max_length=500, null=True, blank=True)
    
    agency_name = models.CharField(max_length=500, null=True, blank=True)
    agency_email = models.CharField(max_length=500, null=True, blank=True)
    agency_phone = models.CharField(max_length=500, null=True, blank=True)
    agency_id = models.IntegerField(null=True, blank=True)
    agency_image = models.CharField(max_length=500, null=True, blank=True)
    agency_website = models.CharField(max_length=500, null=True, blank=True)
    
    agency_json = models.JSONField()
    agent_json = models.JSONField()
    status = models.CharField(max_length=500, default="New")
    
    def __str__(self):
        return str(self.agent_id)
    
    
    
    