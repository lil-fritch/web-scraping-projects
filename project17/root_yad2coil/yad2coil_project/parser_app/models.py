from django.db import models

class Agent(models.Model):
    name = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(unique=True)
    photo_url = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.name