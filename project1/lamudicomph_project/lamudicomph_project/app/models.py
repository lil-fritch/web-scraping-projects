from django.db import models

class Page(models.Model):
    link = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=4, default='New')
    
    def __str__(self):
        return self.link

class Agent(models.Model):
    url = models.CharField(max_length=500, unique=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    agency = models.CharField(max_length=500, blank=True, null=True)
    agency_logo = models.CharField(max_length=500, blank=True, null=True)
    photo = models.CharField(max_length=500, blank=True, null=True)
    is_verified = models.BooleanField(blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    phone2 = models.CharField(max_length=500, blank=True, null=True)
    member_since = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Agent'