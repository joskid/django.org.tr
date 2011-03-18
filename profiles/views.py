# -*- coding: utf-8 -*-
from datetime import datetime, date, timedelta
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django import forms
from profiles.models import *
from django.views.generic.list_detail import object_list
from django import forms
from blog.models import Entry

def profile_list(request):
    queryset = Profile.objects.all()
    city_id = request.GET.get('city')
    
    if city_id:    
        queryset = queryset.filter(city__id=city_id)
    if city_id=='0':
        queryset = Profile.objects.all()
    cities = City.objects.all()
    return object_list(request, queryset=queryset,
                       template_name = 'profiles/profile_list.html',
                       extra_context={'cities':cities})

def profile_detail(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    return render_to_response('profiles/profile_detail.html',
                              {'profile' : profile},
                               context_instance=RequestContext(request))

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

@login_required
def profile_form(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.get_profile())
        if form.is_valid():
            profile = form.save()
            return HttpResponseRedirect(profile.get_absolute_url())
    else:
        form = ProfileForm()
    return render_to_response('profiles/profile_form.html',
                              {'form': form},
                              context_instance=RequestContext(request))
    