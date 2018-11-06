from django.contrib import admin

# Register your models here.

from BC.models import District, OffenseCode, Incident, IncidentLocation, IncidentTime, PoliceStation, PsLocation
from django.contrib import admin

admin.site.register(District)
admin.site.register(OffenseCode)
admin.site.register(Incident)
admin.site.register(IncidentLocation)
admin.site.register(IncidentTime)
admin.site.register(PoliceStation)
admin.site.register(PsLocation)
