# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from utils import slugify
from datetime import datetime

class Entry(models.Model):
    title = models.CharField(max_length = 200)
    teaser = models.TextField(blank=True, null=True)
    body = models.TextField()
    slug = models.SlugField(editable=False, unique=True)
    added = models.DateTimeField(editable = False, auto_now_add=True)
    modified = models.DateTimeField(editable = False, auto_now=True)
    user = models.ForeignKey(User, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Entry, self).save()
   
    @models.permalink        
    def get_absolute_url(self):
        return ('entry_detail', (),
                {'entry_slug': self.slug})

