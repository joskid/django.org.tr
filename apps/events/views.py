from django.views.generic import DetailView
from django.views.generic import ListView
from apps.events.models import Event


class EventList(ListView):
    template_name = 'events/event_list.html'
    model = Event


class EventDetail(DetailView):
    template_name = 'events/event_detail.html'
    model = Event

    def get_context_data(self, **kwargs):
        context = super(EventDetail, self).get_context_data(**kwargs)
        context.update({
            'events': self.model.objects.all()
        })

        return context
