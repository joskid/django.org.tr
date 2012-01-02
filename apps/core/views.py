from django.views.generic import TemplateView
from apps.blog.models import Entry
from apps.core.settings import ENTRY_COUNT
from apps.core.settings import EVENT_COUNT
from apps.core.settings import WEBSITE_COUNT
from apps.events.models import Event
from apps.websites.models import WebSite


class CoreIndex(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(CoreIndex, self).get_context_data(**kwargs)
        context.update({
            'entries': Entry.objects.all()[:ENTRY_COUNT],
            'events': Event.objects.filter(active=True)[:EVENT_COUNT],
            'sites': WebSite.objects.all()[:WEBSITE_COUNT]
        })

        return context
