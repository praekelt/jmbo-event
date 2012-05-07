from django.contrib import admin

from jmbo.admin import ModelBaseAdmin
from event.models import Event, Location, Venue

admin.site.register(Event, ModelBaseAdmin)
admin.site.register(Location)
admin.site.register(Venue)
