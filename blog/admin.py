from django.contrib import admin
from blog.models import *


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'keywords')

admin.site.register(Blog, BlogAdmin)

class EntryAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'added')

admin.site.register(Entry, EntryAdmin)

