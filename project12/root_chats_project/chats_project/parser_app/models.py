from django.db import models
from django.contrib.postgres.fields import ArrayField


class Conversation(models.Model):
    
    conversation_id = models.CharField(max_length=250, unique=True)
    link = models.CharField(max_length=250, null=True, blank=True)

    status = models.CharField(max_length=25, default='New')

    def __str__(self):
        return self.conversation_id

    class Meta:
        verbose_name = 'Conversation'
        verbose_name_plural = 'Conversations' 
        
class ConversationData(models.Model):
    conversation_id = models.CharField(max_length=500, unique=True)
    contact_name = models.CharField(max_length=500, null=True, blank=True)
    contact_id = models.CharField(max_length=500, null=True, blank=True)
    agents = models.JSONField(null=True, blank=True)
    labels = models.JSONField(null=True, blank=True)
    conversation_subject = models.CharField(max_length=500, null=True, blank=True)
    conversation_type = models.CharField(max_length=500, null=True, blank=True)
    conversation_status = models.CharField(max_length=500, null=True, blank=True)
    unread_count = models.IntegerField(null=True, blank=True)
    archived_at = models.DateTimeField(null=True, blank=True)
    highlighted = models.BooleanField(default=False)
    messages = models.JSONField(null=True, blank=True)
    statuses = models.JSONField(null=True, blank=True)
    
    conversation_json = models.JSONField()
    messages_json = models.JSONField(null=True, blank=True)
    status = models.CharField(max_length=25, default='New')
    
    def __str__(self):
        return self.conversation_id

    
    