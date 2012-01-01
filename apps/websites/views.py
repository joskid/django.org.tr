# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.views.generic.list_detail import object_list
from apps.websites.models import WebSite

def website_list(request):

    queryset = WebSite.objects.all().order_by('-start')

    return object_list(request, queryset=queryset,
                       template_name = 'websites/website_list.html')# Create your views here.
