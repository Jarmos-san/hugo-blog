#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

AUTHOR = "Somraj Saha"
SITENAME = "Jarmos's Blog"
SITEURL = "https://jarmos.netlify.app"

PATH = "content"

TIMEZONE = "Asia/Kolkata"

DEFAULT_LANG = "en"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = "feeds/all.atom.xml"
# CATEGORY_FEED_ATOM = None
# TRANSLATION_FEED_ATOM = None
# AUTHOR_FEED_ATOM = None
# AUTHOR_FEED_RSS = None

THEME = "themes/blue-penguin"

# Social widget
# SOCIAL = (
#     ("linkedin", "https://www.linkedin.com/in/jarmos"),
#     ("github", "https://github.com/Jarmos-san"),
#     ("twitter", "https://twitter.com/Jarmosan"),
# )

# DEFAULT_PAGINATION = 2

STATIC_PATHS = [
    "static/favicon.ico",
]

EXTRA_PATH_METADATA = {
    "static/favicon.ico": {"path": "favicon.ico"},
}

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Optional & all blue-penguin specific settings
# all the following settings are *optional*

# HTML metadata
SITEDESCRIPTION = "Somraj's Thoughts & Learning as a Machine Learning Engineer"

# all defaults to True.
DISPLAY_HEADER = True
DISPLAY_FOOTER = True
DISPLAY_HOME = True
DISPLAY_MENU = True

# provided as examples, they make ‘clean’ urls. used by MENU_INTERNAL_PAGES.
TAGS_URL = "tags"
TAGS_SAVE_AS = "tags/index.html"
AUTHORS_URL = "authors"
AUTHORS_SAVE_AS = "authors/index.html"
CATEGORIES_URL = "categories"
CATEGORIES_SAVE_AS = "categories/index.html"
ARCHIVES_URL = "archives"
ARCHIVES_SAVE_AS = "archives/index.html"

# use those if you want pelican standard pages to appear in your menu
MENU_INTERNAL_PAGES = (
    # ("Tags", TAGS_URL, TAGS_SAVE_AS),
    # ("Authors", AUTHORS_URL, AUTHORS_SAVE_AS),
    ("Categories", CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ("Archives", ARCHIVES_URL, ARCHIVES_SAVE_AS),
)
# additional menu items
# MENUITEMS = (
#     ("GitHub", "https://github.com/"),
#     ("Linux Kernel", "https://www.kernel.org/"),
# )
