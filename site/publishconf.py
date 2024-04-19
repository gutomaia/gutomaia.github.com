#!/usr/bin/env python

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://gutomaia.net'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""

GOOGLE_ADSENSE = {
    'ca_id': 'ca-pub-8039666399992046',    # Your AdSense ID
    'page_level_ads': True,                # Allow Page Level Ads (mobile)
    'ads': {
        'main_menu': '2727902218',         # Banner before main menu (all pages)
        'index_top': '8634835017',         # Banner after main menu (index only)
        'index_bottom': '1111568215',      # Banner before footer (index only)
        'article_top': '2588301415',       # Banner after article title (article only)
        'article_bottom': '4065034611',    # Banner after article content (article only)
    }
}

GOOGLE_ANALYTICS = "UA-32666248-1"
