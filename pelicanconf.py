# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'dgrift'
SITENAME = 'My Blog'
SITEURL = 'https://dgrift.home.xs4all.nl'

PATH = 'content'

TIMEZONE = 'Europe/Amsterdam'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'feeds/all_atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = 'feeds/{slug}.atom.xml'
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Github', 'https://github.com/doverride/myblog'),
    ('Fedora DSSP2 RPM repository', "https://dgrift.home.xs4all.nl/dssp2"),)

# Social widget
SOCIAL = (('Twitter', 'https://twitter.com/moverride'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
