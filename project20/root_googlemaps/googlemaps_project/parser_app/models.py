from django.db import models
from django.db.models import JSONField
from django.contrib.postgres.fields import ArrayField


class Zip(models.Model):
    name = models.CharField(max_length=250, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.CharField(max_length=250, null=True, blank=True)

    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords' 
    

class Keyword(models.Model):

    country = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.CharField(max_length=250, null=True, blank=True)

    category = models.CharField(max_length=250, null=True, blank=True)
    name = models.CharField(max_length=250, null=True, blank=True)
    link = models.CharField(max_length=1000)

    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Keyword'
        verbose_name_plural = 'Keywords' 
        

class Link(models.Model):

    country = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.CharField(max_length=250, null=True, blank=True)

    category = models.CharField(max_length=250, null=True, blank=True)
    keyword = models.CharField(max_length=250, null=True, blank=True)

    name = models.CharField(max_length=250)
    link = models.CharField(max_length=1000, unique=True)
    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links' 


class Place(models.Model):
        
    category = models.CharField(max_length=250, null=True, blank=True)
    keyword = models.CharField(max_length=250, null=True, blank=True)
    
    name = models.CharField(max_length=250)

    rating = models.CharField(max_length=250, null=True, blank=True)
    num_reviews = models.CharField(max_length=250, null=True, blank=True)
    reviews_list = JSONField(null=True, blank=True)

    about = ArrayField(models.TextField(), blank=True, null=True)
    
    full_address = models.CharField(max_length=1000, null=True, blank=True)
    country = models.CharField(max_length=250, null=True, blank=True)
    state = models.CharField(max_length=250, null=True, blank=True)
    zip_code = models.CharField(max_length=250, null=True, blank=True)
    city = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, null=True, blank=True)
    located_in = models.CharField(max_length=250, null=True, blank=True)
    lat = models.CharField(max_length=50, null=True, blank=True)
    lng = models.CharField(max_length=50, null=True, blank=True)

    place_type = models.CharField(max_length=250, null=True, blank=True)
    open_hours = models.CharField(max_length=250, null=True, blank=True)
    open_24_7 = models.CharField(max_length=250, null=True, blank=True)

    phone = models.CharField(max_length=500, null=True, blank=True)
    website = models.CharField(max_length=2000, null=True, blank=True)
    email = models.CharField(max_length=500, null=True, blank=True)
    instagram = models.CharField(max_length=500, null=True, blank=True)
    facebook = models.CharField(max_length=500, null=True, blank=True)
    twitter = models.CharField(max_length=500, null=True, blank=True)
    linkedin = models.CharField(max_length=500, null=True, blank=True)

    link = models.CharField(max_length=1000, unique=True)
    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'
