#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Somraj Saha'
SITENAME = 'Blog | Jarmos'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

THEME = 'pelican-themes/pelican-blue'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/jarmos'),
    ('github', 'https://github.com/jarmos-san'),
    ('twitter', 'https://twitter.com/jarmosan')
)

DEFAULT_PAGINATION = 5

STATIC_PATHS = [
    'static/favicon.ico',
    ]
EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
    }

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
