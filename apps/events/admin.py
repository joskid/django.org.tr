from django.contrib import admin
from apps.events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'address', 'start', 'is_published')
admin.site.register(Event, EventAdmin)
