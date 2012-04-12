Date: 2012-04-11 18:52
Tags: pelican, markdown, git, github, blog
Title: Static file blog with Pelican, Twitter Bootstrap, and Github
Slug: pelican-blog-setup

## Preface 

Let me preface this article as not as much a how-to, but more of a learning experience. I go step by step through what I did to get this static blog going, and didn't take out any of the mistakes I made. So read the article before attempting! Let this be your warning.

## Introduction

I won't get into why I chose Pelican beyond that I wanted my blog to be based on Python (personal preference) and use [Jinja2](http://jinja.pocoo.org/docs/) for templating. I've used a little Jinja2 previously and it is an excellent template language. I chose Github because it's free (thanks, guys!) And Twitter Bootstrap is the current de-facto site design boilerplate.

## The Environment

For Python I use [virtualenv](http://pypi.python.org/pypi/virtualenv) and [virtualenvwrapper](http://pypi.python.org/pypi/virtualenvwrapper/) to keep my environments clean so let's begin by creating one.

``` shell
mkvirtualenv pelican --no-site-packages
pip install pelican
pip install markdown
```

You'll also notice I plan on writing in markdown, it is currently a little more universal than restructured text. Pelican will use markdown as long as the package is installed.

``` shell
mkdir blog-environment; cd blog-environment
pip freeze -v >> requirements.txt
```

Finally, allow others to reuse this environment by spitting the dependencies into a requirements file.

## Git

My goal, if possible, is to split up the blog creation environment from the generated content. I also found that there have been a few Twitter Bootstrap themes that I can fork to my liking. For these purposes I will use git submodules.

``` shell
git init
git submodule add https://github.com/ametaireau/pelican-themes
git submodule init
git submodule update
```

Poking around in the bootstrap themes in this repository made apparent that the one I would like to use, Bootstrap2, is not all that polished. Instead of going ahead and fixing it up, I found there is already a pull request in Github waiting to be merged that did exactly what I want. Using the minified version of bootstrap as well as some other good practices.

``` shell
cd pelican-themes/
git remote add stephane https://github.com/stephane/pelican-themes.git
git pull stephane master
```

Thank you, [Stephane Raimbault](https://github.com/stephane). And because I'm going to be hacking up the theme for myself, a simple fork and remote will work out nice...

``` shell
cd pelican-themes
git remote rename origin upstream
git remote add origin git@github.com:zgohr/pelican-themes.git
git push origin master
cd ..
```

``` shell
mkdir output
git submodule add git@github.com:zgohr/zgohr.github.com.git output/
git submodule init
git submodule update
```

Finally, I turned pelican's output directory into my github [page](http://help.github.com/pages/) so changes can be pushed easily. If you would like to fork my blog-environment repository, you'll want to whack this submodule and add your own github page.

## Setting up Pelican

``` shell
wget https://raw.github.com/ametaireau/pelican/master/samples/pelican.conf.py -O settings.py

mkdir content # To store articles as well as static files
mkdir content/extra # robots, humans, favico, etc
wget https://raw.github.com/ametaireau/pelican/master/samples/content/extra/robots.txt -O ./content/extra/robots.txt
```

I then modified my settings file to my liking, and gave it a whirl ```pelican -s settings.py```

This command spits out the static blog into the ```output/``` directory. Loading it up in Chrome and at first glance. Everything looks very nice.
On second glance, not so much.

## Troubleshooting

First, I noticed that in the article metadata, the links aren't working. Clicking my name should take me to the author page and it instead is linking to the relative root.

---

![article infos](images/article_infos.png)

---

I inspected the element and grepped my theme directory for the "By" span label and it is found in ```templates/article_infos.html```.
A quick comparison with some of the other themes shows a discrepency.

My theme is using the ```{{ article.author.url }}``` tag while the others use ```author/{{ article.author }}.html```

My article author doesn't have a url property! Luckily I made a pretty quick assumption that it was due to an incompatibility and when I changed it to look like the other themes, it just worked.

What now, use a theme not optimized for my version of Pelican or update my Pelican to a development version?

## Development Version

If I didn't want to use the latest and greatest version of Twitter Bootstrap, and if I wasn't willing to debug my own issues, I would not have chosen this route.

Let's get the development version installed.

First I modified my ```requirements.txt```. I changed the pelican line from ```pelican==2.8.0``` to ```git+git://github.com/ametaireau/pelican.git```

``` shell
pip uninstall pelican; pip install -r requirements.txt
```

I checked out the theme files I had modified to put them back to the new URL style. Running pelican now gives a bunch of confusing looking errors...

```
WARNING: Found deprecated `ARTICLE_PERMALINK_STRUCTURE` in settings.  Modifing the following settings for the same behaviour.
WARNING: ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%Y}/{date:%m}/{slug}.html'
WARNING: ARTICLE_LANG_URL = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
WARNING: PAGE_URL = '{date:%Y}/{date:%m}/pages/{slug}.html'
WARNING: PAGE_LANG_URL = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
WARNING: ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}.html'
WARNING: ARTICLE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/{slug}-{lang}.html'
WARNING: PAGE_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}.html'
WARNING: PAGE_LANG_SAVE_AS = '{date:%Y}/{date:%m}/pages/{slug}-{lang}.html'
```

Not only that, now my article links are broken.
A quick look at the Pelican 3.0 [docs](http://pelican.notmyidea.org/en/latest/settings.html#url-settings) show there two new important settings called ```ARTICLE_URL``` and ```ARTICLE_SAVE_AS```.
These settings lets you save the static file as a different name than where its links point to. This is nice so your links go directly to a pretty slug, while the page gets saved as an index.html.

The update for settings.py is as follows:

```
ARTICLE_URL = '/posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '/posts/{date:%Y}/{date:%m}/{slug}/index.html'
```

## Conclusion

This has been a learning experience, but nothing too complex to handle. In the future I will have more comments regarding Pelican theming, but until then you'll have to deal with a relatively dirty looking base theme.

Leave a comment if you got some use out of this or need a clarification.

Fork the [blog environment](https://github.com/zgohr/blog-environment)
