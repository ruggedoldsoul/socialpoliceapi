from django.contrib import admin
from .models import Officer,Citizen,Agency,Message
# Register your models here.
from reports.models import Incident,Report,ThreatLevel,Status


admin.site.register(Officer)
admin.site.register(Citizen)
admin.site.register(Agency)
admin.site.register(Message)
admin.site.register(Status)
admin.site.register(Incident)

admin.site.register(ThreatLevel)
admin.site.register(Report)

