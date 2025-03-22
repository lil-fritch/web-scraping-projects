from django.db import models

class Agent(models.Model):
    agent_id = models.IntegerField(unique=True)
    agency_id = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=500, blank=True, null=True)
    phone_extension = models.CharField(max_length=500, blank=True, null=True)
    mobile_phone_number = models.CharField(max_length=500, blank=True, null=True)
    mobile_phone_extension = models.CharField(max_length=500, blank=True, null=True)
    virtual_phone_number = models.CharField(max_length=500, blank=True, null=True)
    virtual_phone_extension = models.CharField(max_length=500, blank=True, null=True)
    position = models.CharField(max_length=500, blank=True, null=True)
    photo_url = models.CharField(max_length=500, blank=True, null=True)
    is_using_sms = models.BooleanField(blank=True, null=True)
    is_using_whatsapp = models.BooleanField(blank=True, null=True)
    is_allowing_remote_calls = models.BooleanField(blank=True, null=True)
    experience_since = models.IntegerField(blank=True, null=True)
    description_de = models.TextField(blank=True, null=True)
    description_en = models.TextField(blank=True, null=True)
    description_fr = models.TextField(blank=True, null=True)
    languages = models.CharField(max_length=500, blank=True, null=True)
    instagram_link = models.CharField(max_length=500, blank=True, null=True)
    facebook_link = models.CharField(max_length=500, blank=True, null=True)
    twitter_link = models.CharField(max_length=500, blank=True, null=True)
    linkedin_link = models.CharField(max_length=500, blank=True, null=True)
    locale = models.CharField(max_length=500, blank=True, null=True)
    
    json_data = models.JSONField(blank=True, null=True)
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self):
        return str(self.agent_id)

class Agency(models.Model):
    agency_id = models.IntegerField(unique=True)
    agency_name = models.CharField(max_length=500, blank=True, null=True)
    account_site = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    addresses = models.CharField(max_length=500, blank=True, null=True)
    recommendations = models.IntegerField(blank=True, null=True)
    facets_buy = models.IntegerField(blank=True, null=True)
    facets_rent = models.IntegerField(blank=True, null=True)
    facets_sold = models.IntegerField(blank=True, null=True)
    followers = models.IntegerField(blank=True, null=True)
    logo_url = models.CharField(max_length=500, blank=True, null=True)
    
    json_data = models.JSONField()
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self):
        return str(self.agency_id)