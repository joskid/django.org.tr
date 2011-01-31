from django.contrib import admin
from profiles.models import Profile, City


class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(City, CityAdmin)

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'name')
admin.site.register(Profile, ProfileAdmin)
