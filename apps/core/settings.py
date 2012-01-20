from django.conf import settings

FEEDS_COUNT = getattr(settings, 'CORE_FEEDS_COUNT', 5)
EVENT_COUNT = getattr(settings, 'CORE_EVENT_COUNT', 5)
WEBSITE_COUNT = getattr(settings, 'CORE_EVENT_COUNT', 10)
