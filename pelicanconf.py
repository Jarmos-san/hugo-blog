#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

AUTHOR = 'Somraj Saha'
SITENAME = "Jarmos's Blog"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Asia/Kolkata'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'pelican-themes/pelican-blue'

# Social widget
SOCIAL = (
    ('linkedin', 'https://www.linkedin.com/in/jarmos'),
    ('github', 'https://github.com/Jarmos-san'),
    ('twitter', 'https://twitter.com/Jarmosan')
)

DEFAULT_PAGINATION = 6

STATIC_PATHS = [
    'static/favicon.ico',
]

EXTRA_PATH_METADATA = {
    'static/favicon.ico': {'path': 'favicon.ico'},
}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

SIDEBAR_DIGEST = 'Machine Learning Engineer'

DISPLAY_PAGES_ON_MENU = True

# TWITTER_USERNAME = 'jarmosan'

MENUITEMS = (
    ('Blog', SITEURL),
)
