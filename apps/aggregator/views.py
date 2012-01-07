from __future__ import absolute_import

import logging
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic.list_detail import object_list
from .models import FeedItem, Feed
from .forms import FeedModelForm

from apps.aggregator.shortcuts import render


def index(request):
    """
    Displays the latest feeds of each type.
    """
    ctx = {'item_list': FeedItem.objects.all()}
    return render(request, 'aggregator/index.html', ctx)


def feed_list(request, feed_type_slug):
    """
    Shows the latest feeds for the given type.
    """
    feed_type = get_object_or_404(FeedType, slug=feed_type_slug)
    return object_list(request,
        queryset = FeedItem.objects.filter(feed__feed_type=feed_type),
        paginate_by = 25,
        extra_context = {'feed_type': feed_type},
    )
