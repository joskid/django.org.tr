# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from utils import slugify
from datetime import datetime

'''
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    description = models.CharField(max_length = 200, blank=True, null=True)
    keywords = models.CharField(max_length = 200, blank=True, null=True)
    slug = models.SlugField(editable=False, unique=True)
    
    def __unicode__(self):
        return self.title

    class Admin:
        pass

    def save(self):
        self.slug = slugify(self.title)
        super(Blog, self).save()
            
    @models.permalink
    def get_absolute_url(self):
        return ('blog_detail', (),
                {'blog_slug': self.slug})

'''
class Entry(models.Model):
    #blog = models.ForeignKey(Blog)
    title = models.CharField(max_length = 200)
    teaser = models.TextField(blank=True, null=True)
    body = models.TextField()
    slug = models.SlugField(editable=False, unique=True)
    added = models.DateTimeField(editable = False)
    modified = models.DateTimeField(editable = False)
    user = models.ForeignKey(User, related_name='blog_entry_set',
                             blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)

    def __unicode__(self):
        return self.title

    def save(self):
        now = datetime.now()
        self.modified = now
        if not self.id:
            self.added = now
        self.slug = slugify(self.title)
        super(Entry, self).save()
   
    @models.permalink        
    def get_absolute_url(self):
        return ('entry_detail', (),
                {'entry_slug': self.slug})

