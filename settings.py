# -*- coding: utf-8 -*-
AUTHOR = 'Zach Gohr' 
SITENAME = 'Return the Videotapes'
SITEURL = 'http://zgohr.github.com'
TIMEZONE = 'America/Chicago' 
ARTICLE_URL = '/posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '/posts/{date:%Y}/{date:%m}/{slug}/index.html'
THEME = './pelican-themes/bootstrap2'
PATH = './content'

GITHUB_URL = 'http://github.com/zgohr/'
DISQUS_SITENAME = 'returnthevideotapes' 
GOOGLE_ANALYTICS = 'UA-30789241-1' 
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = ""
DEFAULT_PAGINATION = 4
DEFAULT_CATEGORY = 'rant'
TWITTER_USERNAME = 'zgohr'

FEED_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('Ron Buchanan', 'http://ron.notbuckman.com/whats-new/'),)

SOCIAL = (('twitter', 'http://twitter.com/zgohr'),
          ('github', 'http://github.com/zgohr'),
          ('facebook', 'http://www.facebook.com/zgohr'),)

STATIC_PATHS = ["images",]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
