from django.db import models

class Agent(models.Model):
    agent_id = models.CharField(unique=True)
    status = models.CharField(default='New', max_length=4)
    json_data = models.JSONField()
    
    agents_of_excellence_rank = models.IntegerField(blank=True, null=True)
    blog_url = models.CharField(max_length=501, blank=True, null=True)
    email = models.CharField(max_length=500, blank=True, null=True)
    facebook_url = models.CharField(max_length=500, blank=True, null=True)
    first_name = models.CharField(max_length=500, blank=True, null=True)
    image = models.CharField(max_length=500, blank=True, null=True)
    job_title = models.CharField(max_length=500, blank=True, null=True)
    last_name = models.CharField(max_length=500, blank=True, null=True)
    linkedin_url = models.CharField(max_length=500, blank=True, null=True)
    listing_count = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    office_brand_hex_code = models.CharField(max_length=500, blank=True, null=True)
    office_image = models.CharField(max_length=500, blank=True, null=True)
    office_is_brand_colour_light = models.BooleanField(blank=True, null=True)
    office_name = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=500, blank=True, null=True)
    phone_ddi = models.CharField(max_length=500, blank=True, null=True)
    phone_mobile = models.CharField(max_length=500, blank=True, null=True)
    show_profile = models.BooleanField(blank=True, null=True)
    slug = models.CharField(max_length=500, blank=True, null=True)
    twitter_url = models.CharField(max_length=500, blank=True, null=True)
    website_url = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
        return self.agent_id