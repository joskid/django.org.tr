from django.views.generic import DateDetailView
from django.views.generic import ListView
from apps.events.models import Event


class EventIndex(ListView):
    template_name = 'events/index.html'
    queryset = Event.objects.filter(is_published=True)


class EventDetail(DateDetailView):
    template_name = 'events/detail.html'
    model = Event
    month_format = '%m'
    allow_future = True
    date_field = 'start'

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context.update({
            'events': self.model.objects.all()
        })

        return context
