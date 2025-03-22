from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    status = models.CharField(max_length=500, default='New')

    def __str__(self):
        return self.name
    
class Page(models.Model):
    url = models.CharField(max_length=500, unique=True)
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self):
        return self.url
    
class Agent(models.Model):
    url = models.CharField(max_length=500, unique=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    phones = models.CharField(max_length=500, blank=True, null=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    facebook = models.CharField(max_length=1000, blank=True, null=True)
    instagram = models.CharField(max_length=1000, blank=True, null=True)
    youtube = models.CharField(max_length=1000, blank=True, null=True)
    linkedin = models.CharField(max_length=1000, blank=True, null=True)
    logo = models.CharField(max_length=500, blank=True, null=True)
    banner = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.title