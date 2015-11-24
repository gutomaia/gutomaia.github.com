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

MENUITEMS = [
    ('1pyNES', '/pyNES'),
    ('2nodeNES', '/nodeNES'),
]


STATIC_PATHS = ['images', join('extra', 'CNAME')]
EXTRA_PATH_METADATA = {join('extra', 'CNAME'): {'path': 'CNAME'},}

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "../Flex"

#Flex Theme Specific
SITETITLE = 'gutomaia'
SITESUBTITLE = 'Pythonist with a NES and an ☂'
SITELOGO = 'https://s.gravatar.com/avatar/760d34405db2c028a3fb099a4510d870?s=100'
COPYRIGHT_YEAR = 2015
