from django.db import models
from django.contrib.postgres.fields import ArrayField

class Business(models.Model):
    business_id = models.CharField(unique=True)
    business_url = models.CharField(max_length=500, blank=True, null=True)
    business_type = models.CharField(max_length=500, blank=True, null=True)
    city = models.CharField(max_length=500, blank=True, null=True)
    name = models.CharField(max_length=500, blank=True, null=True)
    phone_number = models.CharField(max_length=500, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)
    review_count = models.IntegerField(blank=True, null=True)
    stars_1 = models.IntegerField(blank=True, null=True)
    stars_2 = models.IntegerField(blank=True, null=True)
    stars_3 = models.IntegerField(blank=True, null=True)
    stars_4 = models.IntegerField(blank=True, null=True)
    stars_5 = models.IntegerField(blank=True, null=True)
    website = models.CharField(max_length=500, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    rewritten_description = models.TextField(blank=True, null=True)
    year_established = models.CharField(max_length=500, blank=True, null=True)
    history = models.TextField(blank=True, null=True)
    read_more_url = models.CharField(max_length=500, blank=True, null=True)
    address_line_1 = models.CharField(max_length=500, blank=True, null=True)
    address_line_2 = models.CharField(max_length=500, blank=True, null=True)
    address_line_3 = models.CharField(max_length=500, blank=True, null=True)
    postal_code = models.CharField(max_length=500, blank=True, null=True)
    photo_url = models.CharField(max_length=500, blank=True, null=True)
    logo_url = models.CharField(max_length=500, blank=True, null=True)
    categories = models.CharField(max_length=500, blank=True, null=True)
    currency_code = models.CharField(max_length=500, blank=True, null=True)
    yelp_menu = models.CharField(max_length=500, blank=True, null=True)
    operation_hours = models.CharField(max_length=500, blank=True, null=True)
    chain_biz_info = models.CharField(max_length=500, blank=True, null=True)
    photos = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    
    status = models.CharField(max_length=500, default='New')
    json_data = models.JSONField(blank=True, null=True)
    json_data_description = models.JSONField(blank=True, null=True)
    json_data_search = models.JSONField(blank=True, null=True)
    
    def __str__(self):
        return self.business_id

class Review(models.Model):
    review_id = models.CharField(unique=True)
    business = models.ForeignKey(Business, to_field='business_id', on_delete=models.CASCADE)
    business_name = models.CharField(max_length=500, blank=True, null=True)
    language = models.CharField(max_length=500, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    created_at = models.CharField(max_length=500, blank=True, null=True)
    rating = models.IntegerField(blank=True, null=True)
    author_id = models.CharField(max_length=500, blank=True, null=True)
    author_name = models.CharField(max_length=500, blank=True, null=True)
    author_total_count_reviews = models.IntegerField(blank=True, null=True)
    author_is_elite = models.BooleanField(blank=True, null=True)
    count_thanks_reactions = models.IntegerField(blank=True, null=True)
    count_useful_reactions = models.IntegerField(blank=True, null=True)
    count_love_this_reactions = models.IntegerField(blank=True, null=True)
    count_oh_no_reactions = models.IntegerField(blank=True, null=True)
    photos = ArrayField(models.CharField(max_length=500), blank=True, null=True)
    
    json_data = models.JSONField()
    status = models.CharField(max_length=500, default='New')
    
    def __str__(self) -> str:
        return self.review_id

class Search(models.Model):
    decs = models.CharField(max_length=500, blank=True, null=True)
    category = models.CharField(max_length=500, blank=True, null=True)
    postal_code = models.CharField(max_length=500, blank=True, null=True)
    
    status = models.CharField(max_length=500, default='New')
    
    class Meta:
        unique_together = ('decs', 'category', 'postal_code')
    
    def __str__(self):
        return f'{self.decs} - {self.category} - {self.postal_code}'
    
class SearchWitoutCategory(models.Model):
    decs = models.CharField(max_length=500, blank=True, null=True)
    postal_code = models.CharField(max_length=500, blank=True, null=True)
    
    status = models.CharField(max_length=500, default='New')
    
    class Meta:
        unique_together = ('decs', 'postal_code')
    
    def __str__(self):
        return f'{self.decs} - {self.postal_code}'