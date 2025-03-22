from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=500)
    url = models.CharField(max_length=500)
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self):
        return self.name

class Agent(models.Model):
    agent_id = models.IntegerField(unique=True)
    first_name = models.CharField(max_length=500, null=True, blank=True)
    last_name = models.CharField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=500, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    agency = models.CharField(max_length=500, null=True, blank=True)
    profile_image = models.CharField(max_length=500, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'