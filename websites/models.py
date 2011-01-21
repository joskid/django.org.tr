# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from utils import slugify
    

class WebSite(models.Model):
    name = models.CharField('İsim', max_length=100, blank=True, null=True)
    about = models.CharField('Genel Bilgi', max_length=150, blank=True, null=True)
    url = models.URLField('Web sitesi', blank=True, null=True)

    def __unicode__(self):
        return self.name
    