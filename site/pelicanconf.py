#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from os.path import join

AUTHOR = u'Guto Maia'
SITENAME = u'gutomaia'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('pyNES', '/pyNES'),
    ('nodeNES', '/nodeNES'),
)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/gutomaia'),
          ('github', 'http://github.com/gutomaia'),
          ('linkedin', 'http://linkedin.com/in/gutomaia')
          )

DEFAULT_PAGINATION = 10


STATIC_PATHS = ['images', join('extra', 'CNAME')]
EXTRA_PATH_METADATA = {join('extra', 'CNAME'): {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
