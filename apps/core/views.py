from datetime import datetime
from django.views.generic import TemplateView
from apps.core.settings import WEBSITE_COUNT
from apps.events.models import Event
from apps.websites.models import WebSite


class CoreIndex(TemplateView):
    template_name = 'core/index.html'

    def get_context_data(self, **kwargs):
        context = super(CoreIndex, self).get_context_data(**kwargs)
        context.update({
            'events': Event.objects.filter(is_published=True,
                                           start__gt=datetime.now()),
            'sites': WebSite.objects.all()[:WEBSITE_COUNT]
        })

        return context
