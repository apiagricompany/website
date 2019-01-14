#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import date
import sys
sys.path.append('.')

AUTHOR = 'ApiAgri'
SITENAME = 'ApiAgri'
SITEURL = 'apiagri.com'
SITELOGO = 'images/logo.png'
SITELOGOWEBP = 'images/logo.webp'
APPURL = "https://"
THEME = "theme"
PATH = "content"
TIMEZONE = 'America/Sao_Paulo'

PLUGIN_PATHS = ['./plugins/']
PLUGINS = ['sitemap']\

SITEMAP ={
    'format': 'xml'
}

from utils import filters
JINJA_FILTERS={ 'sidebar': filters.sidebar }

DEFAULT_LANG = u'pt_BR'

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
SOCIAL = (('facebook-f', 'https://www.facebook.com/apiagricompany'),
          ('instagram', 'https://www.instagram.com/apiagricompany'),)

MENUITEMS = (('O que é ApiAgri?', '#oquee'),
    ('Como Funciona?', '#como'),
    # ('Baixe o APP', '#download'),
    ('Nossa Equipe', '#equipe'),
    ('Benefícios', '#beneficios'),
    ('Cadastre-se', '#cta'))

#DEFAULT_PAGINATION = 3
#POST_LIMIT = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

DISPLAY_PAGES_ON_MENU = False

# Formatting for urls
# ARTICLE_DIR = 'blog'
ARTICLE_URL = "blog/{slug}"
ARTICLE_SAVE_AS = "blog/{slug}/index.html"

ARCHIVES_URL = "blog"
ARCHIVES_SAVE_AS = "blog/index.html"

PAGE_PATHS = [ 'pages' ]
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

CATEGORY_URL = "category/{slug}/"
CATEGORY_SAVE_AS = "category/{slug}/index.html"

TAG_URL = "tag/{slug}/"
TAG_SAVE_AS = "tag/{slug}/index.html"

USE_FOLDER_AS_CATEGORY = True

# Generate yearly archive
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'

# Show most recent posts first
NEWEST_FIRST_ARCHIVES = True

STATIC_PATHS = [
    'images',
    'fonts',
    'css',
    'js'
]

DISPLAY_BLOG_ON_MENU = False


CURRENTYEAR = date.today().year
