from django.db import models

class Agent(models.Model):
    account_id = models.CharField(max_length=500)
    country = models.CharField(max_length=500, null=True, blank=True)
    state = models.CharField(max_length=500, null=True, blank=True)
    
    account_number = models.CharField(max_length=500, blank=True, null=True)
    email_address = models.CharField(max_length=500, blank=True, null=True)
    telephone_1 = models.CharField(max_length=500, blank=True, null=True)
    telephone_2 = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    cpa_trading_name = models.CharField(max_length=500, blank=True, null=True)
    websiteurl = models.CharField(max_length=500, blank=True, null=True)
    address_composite = models.CharField(max_length=500, blank=True, null=True)
    address_latitude = models.FloatField(blank=True, null=True)
    address_longitude = models.FloatField(blank=True, null=True)
    
    json_data = models.JSONField()
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self):
        return self.account_id
    
    class Meta:
        unique_together = ['account_id', 'country', 'state']