from django.contrib import admin
from apps.planet.models import Feed
from apps.planet.models import FeedItem


class FeedAdmin(admin.ModelAdmin):
    list_display = (
        '__unicode__', 'feed_url', 'site_url', 'is_active', 'owner')
admin.site.register(Feed, FeedAdmin)


class FeedItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'feed', 'published_at')
admin.site.register(FeedItem, FeedItemAdmin)
