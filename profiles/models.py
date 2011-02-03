# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from django.template.loader import get_template
from django.template import Context
from utils import slugify


class City(models.Model):
    name = models.CharField(max_length = 50)

    def __unicode__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, verbose_name='Kullanıcı adı',
                                unique=True, db_index=True)
    name = models.CharField('İsim', max_length=100, blank=True, null=True)
    about = models.TextField('Genel bilgi', blank=True, null=True)
    url = models.URLField('Web sitesi', blank=True, null=True)
    city = models.ForeignKey(City, verbose_name='Şehir')
    photo = models.ImageField('Profil fotoğrafı', upload_to='user_photo/%Y/%m/%d/',
                              blank=True, null=True)

    def __unicode__(self):
        return self.user.username
    
    @models.permalink
    def get_absolute_url(self):
        return ('profile_detail', (),
                {'username' : self.user.username})
        
