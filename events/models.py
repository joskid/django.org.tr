# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from utils import slugify


class Event(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField('Açıklama', blank=True, null=True)
    start = models.DateTimeField('Başlangıç zamanı', db_index=True)
    end = models.DateTimeField('Bitiş zamanı', blank=True, null=True)
    locations = models.TextField('Yer(ler)', max_length=250, blank=True)
    active = models.BooleanField('Geçerli', default=True)
    user = models.ForeignKey(User)
    slug = models.SlugField(editable=False)
    added = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title
    
    def save(self, **kwargs):
        self.slug = slugify(self.title)
        super(Event, self).save(**kwargs)

    @models.permalink
    def get_absolute_url(self):
        return ('event_detail', (),
                {'year':self.start.year,
                 'month':self.start.month,
                 'day':self.start.day,
                 'slug':self.slug})
    
    class Meta:
        ordering = ('-start',)

