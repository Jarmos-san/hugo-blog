#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Somraj'
SITENAME = 'Somraj Saha'
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

# Blogroll
LINKS = (
    ('Blogs', f'{SITEURL}/pages'),
    ('About Me', f'{SITEURL}/author')
)

# Social widget
SOCIAL = (
    ('github', 'https://github.com/jarmos-san/'),
    ('twitter', 'https://twitter.com/Jarmosan'),
    ('linkedin', 'https://www.linkedin.com/in/jarmos/')
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Theme changes
THEME = 'themes'
THEME_COLOR = 'dark'
THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

# Code blocks/pygment changes
PYGMENTS_STYLE = 'emacs'
PYGMENTS_STYLE_DARK = 'monokai'