AUTHOR = 'keneni'
SITENAME = 'Gadget Reveiw Hub'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'English'

# Set the full site URL (with repo name)
SITEURL = 'https://Keneni-Tech.github.io/gadget-hub.io'

# Disable relative URLs so links are generated properly
RELATIVE_URLS = False


import os
THEME = os.path.join(os.path.dirname(__file__), 'pelican-themes', 'zurb-F5-basic')


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

##------------------------
# pelican content -s publishconf.py
# pelican content -o docs -s publishconf.py
