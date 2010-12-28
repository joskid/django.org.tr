from django.contrib import admin
from events.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'start')

admin.site.register(Event, EventAdmin)

