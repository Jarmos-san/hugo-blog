#!/usr/bin/env python3
# -*- coding: utf-8 -*- #

AUTHOR = "Somraj Saha"
SITENAME = "Jarmos's Blog"
SITEURL = ""  # For development
SITEURL = "https://jarmos.netlify.app"  # For production
SITEDESCRIPTION = "Somraj's Thoughts & Learning as a Machine Learning Engineer"
TIMEZONE = "Asia/Kolkata"
DEFAULT_LANG = "en"

PATH = "content"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = "themes/blue-penguin"

STATIC_PATHS = [
    "static/favicon.ico",
]

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
    ("Categories", CATEGORIES_URL, CATEGORIES_SAVE_AS),
    ("Archives", ARCHIVES_URL, ARCHIVES_SAVE_AS),
)

# Pagination
DEFAULT_PAGINATION = True

PAGINATION_PATTERNS = (
    (1, "{url}", "{save_as}"),
    (2, "{base_name}/page/{number}/", "{base_name}/page/{number}/index.html"),
)
