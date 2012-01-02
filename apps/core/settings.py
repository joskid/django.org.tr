from django.conf import settings

ENTRY_COUNT = getattr(settings, 'CORE_ENTRY_COUNT', 5)
EVENT_COUNT = getattr(settings, 'CORE_EVENT_COUNT', 5)
WEBSITE_COUNT = getattr(settings, 'CORE_EVENT_COUNT', 10)
