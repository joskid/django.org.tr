from datetime import datetime
from django.db import models
from time import mktime
from utils import slugify


class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True)
    address = models.TextField(max_length=250, blank=True)
    start = models.DateTimeField(db_index=True)
    is_published = models.BooleanField(default=False)
    slug = models.SlugField(editable=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title

    def save(self, **kwargs):
        self.slug = slugify(self.title)

        return super(Event, self).save(**kwargs)

    @property
    def event_date(self):
        return int(mktime(self.created_at.timetuple()))

    @models.permalink
    def get_absolute_url(self):
        url_dict = {
            'year': self.start.year,
            'month': self.start.month,
            'day': self.start.day,
            'slug': self.slug
        }

        return ('event_detail', (), url_dict)

    class Meta:
        ordering = ('-start',)
