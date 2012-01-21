import logging
from datetime import datetime
from django.core.management.base import BaseCommand
from apps.planet.utils import parse_feed
from apps.planet.models import Feed
from apps.planet.models import FeedItem


class Command(BaseCommand):
    help = "Update feeds"

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.DEBUG)
        feeds = Feed.objects.filter(is_active=True)

        for feed in feeds:
            response = parse_feed(url=feed.feed_url)

            if not response.get('success', False):
                logging.debug('Failure: %s' % feed.feed_url)
            else:
                for entry in response.get('entries', []):
                    try:
                        feed_item = FeedItem.objects.get(
                            feed=feed,
                            title=entry.get('title'),
                            link=entry.get('link'))
                        feed_item.published_at = entry.get('created')
                        feed_item.content = entry.get('content')
                    except FeedItem.DoesNotExist:
                        FeedItem.objects.create(
                            feed=feed,
                            title=entry.get('title'),
                            link=entry.get('link'),
                            published_at=entry.get('created'),
                            content=entry.get('content'))

                logging.debug('Success: %s' % feed.feed_url)

            feed.last_checked = datetime.now()
            feed.save()
