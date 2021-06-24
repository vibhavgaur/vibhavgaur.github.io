#!/usr/bin/env python
# -*- coding: utf-8 -*- #

SITENAME = 'Vibhav Gaur'

## ------------------------------URL Settings------------------------------ ##
# SITEURL = 'https://vibhavgaur.github.io'
SITEURL = ''    # Default

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True      # Default: False -- use relative URLs or not

# ARTICLE_URL =             # Default: '{slug}.html' -- URL to refer to an article
# ARTICLE_SAVE_AS =         # Default: '{slug}.html' -- the place where the article will be saved

# DRAFT_URL =               # Default: 'drafts/{slug}.html'
# DRAFT_SAVE_AS =           # Default: 'drafts/{slug}.html'

# PAGE_URL =                # Default: 'pages/{slug}.html'
# PAGE_SAVE_AS =            # Default: 'pages/{slug}.html'

AUTHOR_SAVE_AS = ''       # Default: author/{slug}.html' -- set to '' so that the Author's page is not generated

# STATIC_CREATE_LINKS =     # Default: False -- don't really know what this does


## ------------------------------Path Settings------------------------------ ##
PATH = './content'
# PAGE_PATHS = ['/pages']   # Default: ['pages']
# ARTICLE_PATHS =           # Default: ['']
# STATIC_PATHS =            # Default: ['images'] -- directory to look for static files
THEME = './theme'
OUTPUT_PATH = 'testOutput/'

## -----------------------------Template Settings----------------------------- ##

# DIRECT_TEMPLATES =        # Default: ['index', 'authors', 'categories', 'tags', 'archives'] -- Not quite sure what this does

## -----------------------------Metadata Settings----------------------------- ##
AUTHOR = 'Vibhav Gaur'
# DEFAULT_METADATA =          # Default: {} -- default metadata used for all articles and pages


## -----------------------------Plugins Settings----------------------------- ##

PLUGIN_PATHS = ['./plugins/plugins']    # directory where to look for plugins
# List of plugins to load
PLUGINS = ['render_math',
            'sitemap'
            ]

LOAD_CONTENT_CACHE = False

## ---------------------------Markdown Settings--------------------------- ##

# Extra config settings for the Markdown processor, specified as a dictionary
# Markdown extensions automatically get processed through the extension_config option
MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'codeBlock'},
        'markdown.extensions.meta': {},
    },
    'output_format': 'html5',
}

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = 'English'
DEFAULT_DATE_FORMAT = '%B %d, %Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS =  (('My GitHub', 'https://github.com/vibhavgaur'),)
 
# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
          # ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# For the website to be indexed on Google
SITEMAP = {
        "format": "xml",
}

## ------------------------------Cache Settings------------------------------ ##
# CACHE_CONTENT =           # Default: False
# CACHE_PATH =              # Default: 'cache'
# GZIP_CACHE =              # Default: True -- compress / decompress cache files using gzip
# LOAD_CONTENT_CACHE =      # Default: False -- load unmodified content from cache
# AUTORELOAD_IGNORE_CACHE = True      # Ignore cache option?

## ------------------------------Other Settings------------------------------ ##

TYPOGRIFY = True            # Some HTML improvements are made if this is true

DEFAULT_DATE_FORMAT = '%B %d, %Y'   # for the whole website



## ------------------------------Jinja Filters------------------------------ ##
# Custom Jinja filters
def get_page(hidden_pages, slug):
    for page in hidden_pages:
        if page.slug == slug:
            return page

def get_article_by_type(articles, inputType):
    projectArticles = []
    for article in articles:
        if article.pagetype == inputType:
            projectArticles.append(article)
    return projectArticles

# Dictionary of custom Jinja 2 filters. Should map the filename to the filter function
JINJA_FILTERS = {
    "get_page": get_page,
    "get_article_by_type": get_article_by_type,
}