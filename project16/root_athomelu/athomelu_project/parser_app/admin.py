from django.contrib import admin

from .models import *

class AgentAdmin(admin.ModelAdmin):
    fields = ['__all__']

class AgencyAdmin(admin.ModelAdmin):
    fields = ['__all__']

admin.site.register(Agent, AgentAdmin)
admin.site.register(Agency, AgencyAdmin)