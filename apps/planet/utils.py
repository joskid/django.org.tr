import feedparser
from hashlib import sha1 as sha
import locale
import logging
import re
from datetime import datetime
from time import mktime

log = logging.getLogger('django_tr.apps.planet.utils')


def parse_feed(url, summary_size=1000):
    response = {
        'feed': None,
        'success': False,
        'entries': [],
        'error': None
    }

    try:
        response.update({
            'feed': feedparser.parse(url)
        })
    except Exception, e:
        response.update({'error': e})
        log.error('Feed parsing failed', exc_info=e)

        return response
    else:
        response.update({'success': True})

    for entry in response.get('feed').entries:
        link = getattr(entry, 'link', '')

        # Do not process entries without title
        if not hasattr(entry, 'title'):
            log.error('Post %s does not has a title' % link)
            continue

        title = entry.title

        if hasattr(entry, 'content'):
            content = entry.content[0].value
        elif hasattr(entry, 'summary'):
            content = entry.summary
        elif hasattr(entry, 'description'):
            content = entry.description
        else:
            # Use title as fallback variant for the post's content
            content = title

        summary = content[:summary_size]

        # summary = clean.safe_html(summary)
        # content = clean.safe_html(content)

        created = parse_modified_date(entry, response.get('feed'))
        if not created:
            log.error('Post %s does not has modified date' % link)
            continue

        guid = sha(link.encode('utf-8')).hexdigest()

        entry = {
            'title': title,
            'link': link,
            'summary': summary,
            'content': content,
            'created': created,
            'guid': guid,
        }

        response.get('entries').append(entry)

    return response


def parse_modified_date(entry, feed):
    """
    Find out modified date of feed entry.
    """

    parsed = []
    unparsed = []

    keys = ['published', 'created', 'updated', 'modified']
    for key in keys:
        value = getattr(entry, '%s_parsed' % key, None)
        if value:
            parsed.append(value)
        value = getattr(entry, key, None)
        if value:
            unparsed.append(value)

    if parsed:
        time_tuple = parsed[0]
        return datetime.fromtimestamp(mktime(time_tuple))

    if unparsed:
        guessed = guess_date(unparsed, feed)
        if guessed:
            return guessed

    return None


def guess_date(dates, feed):
    """
    Try to parse date in non-standart format.
    """

    parsed = None
    oldlocale = locale.getlocale()

    for date_string in dates:
        tz_offset = re.compile(r'\s+\+(\d{2})(\d{2})$')
        match = tz_offset.search(date_string)
        # TODO: implement processing TZ offset
        # and normalizing the date to the project's TZ
        if match:
            date_string = tz_offset.sub('', date_string)
        else:
            pass

        lang = feed.feed.language[:2]
        # strptime fails on unicode
        if isinstance(date_string, unicode):
            date_string = date_string.encode('utf-8')

        if not lang.startswith('en'):
            try:
                locale_name = str('%s_%s.UTF-8' % (lang.lower(), lang.upper()))
                locale.setlocale(locale.LC_ALL, locale_name)
            except locale.Error:
                pass
            # try localized RFC 822 format
            try:
                parsed = datetime.strptime(
                    date_string, '%a, %d %b %Y %H:%M:%S')
            except ValueError:
                pass
            else:
                break
    locale.setlocale(locale.LC_ALL, oldlocale)

    return parsed
