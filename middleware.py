from django.http import Http404, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from encodings.idna import ToUnicode
from utils import slugify
from utils import get_subdomain

current_site = Site.objects.get_current()

class NormalizeSubdomainMiddleware:
    def process_request(self, request):
        subdomain = get_subdomain(request)
        if subdomain == 'www':
            return HttpResponseRedirect('http://%s%s' % (current_site.domain, request.path))
        if subdomain != '':
            slugified = slugify(ToUnicode(subdomain).lower())
            if subdomain != slugified:
                return HttpResponseRedirect('http://%s.%s/' % (slugified, current_site.domain))

class NormalizeTagLinkMiddleware:
    def process_response(self, request, response):
        if response.status_code != 404:
            return response
        parts = request.path[1:].split('/')
        if len(parts) == 0 or (len(parts) > 1 and parts[1] != ''):
            return response
        # the last part can be have the tags
        last_bits = parts[-1].split('+')
        redirect_tag_url_bits = []
        for bit in last_bits:
            redirect_tag_url_bits.append(slugify(bit))
        redirect_tag_url = '+'.join(redirect_tag_url_bits)
        if parts[-1] == redirect_tag_url:
            # already a proper tag slug, but 404
            return response
        parts[-1] = redirect_tag_url
        return HttpResponsePermanentRedirect('/'.join(parts))

