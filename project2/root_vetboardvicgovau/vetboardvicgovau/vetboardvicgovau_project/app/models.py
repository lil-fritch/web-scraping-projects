from django.db import models

class Vet(models.Model):
    name = models.CharField(max_length=500, unique=True)
    address = models.CharField(max_length=500, blank=True, null=True)
    status = models.CharField(max_length=500, blank=True, null=True)
    registration_no = models.CharField(max_length=500, blank=True, null=True)
    endorsed_in = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return self.name