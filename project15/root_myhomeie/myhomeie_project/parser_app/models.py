from django.db import models

class Agent(models.Model):
    agent_id = models.IntegerField(unique=True)
    url = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    seo_name = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    image_url = models.CharField(max_length=500, blank=True, null=True)
    sales_license = models.CharField(max_length=500, blank=True, null=True)
    rental_license = models.CharField(max_length=500, blank=True, null=True)
    is_phone_revealed = models.BooleanField(null=True, blank=True)
    
    json_data = models.JSONField()
    status = models.CharField(max_length=500, default="New")
    
    def __str__(self):
        return str(self.agent_id)