#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Vibhav Gaur'
SITENAME = 'Vibhav Gaur'
SITEURL = ''

PATH = 'content'
# PAGE_PATHS = ['/pages']

LOAD_CONTENT_CACHE = False

DISPLAY_PAGES_ON_MENU = True
MENUITEMS = (
	('Home', ''),
	('Coursework','/pages/coursework.html'),
	('Projects','/pages/projects.html'),
	('Resume','/pages/resume.html'),
	('Blog','/pages/blog.html')
	)

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
LINKS =  (('My GitHub', 'https://github.com/vibhavgaur'),)
 
# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Custom Jinja filter
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
    
JINJA_FILTERS = {
	"get_page": get_page,
    "get_article_by_type": get_article_by_type,
}

