from django.views.generic import ListView
from apps.planet.models import Feed
from apps.planet.models import FeedItem


class PlanetIndex(ListView):
    template_name = 'planet/index.html'
    queryset = FeedItem.objects.filter(feed__is_active=True)
