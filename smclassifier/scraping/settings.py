# -*- coding: utf-8 -*-

# Scrapy settings for smscrapper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'smscrapper'

SPIDER_MODULES = ['smclassifier.scraping.spiders']
NEWSPIDER_MODULE = 'smclassifier.scraping.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.106 Safari/537.36'

# Custom parameter : set cookie to avoid captcha
REQUEST_COOKIES = {
    'datadome': 'MRiPacQ_UskTPibdMaKGficUHpQdamvi-HKmU1Lq9Ro45_Yb_gGYje~2x~ldZnKtpJJrk1Iv69pZ7lYdOyTzj8phrWfFjQn.WSZhZxyhov',
}

# Custom parameter : domain allowed to be crawled
ALLOWED_DOMAINS = ['www.ouest-france.fr']

# Custom parameter : sitemap URLs to crawl
SITEMAP_URLS = ['https://www.ouest-france.fr/sitemap.xml']

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
EXTENSIONS = {
    'scrapy.extensions.closespider.CloseSpider': 300,
}

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 5

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 0.5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

CLOSESPIDER_PAGECOUNT = 50

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'smclassifier.scraping.pipelines.SmscrapperPipeline': 300,
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'smclassifier.scraping.middlewares.SmscrapperSpiderMiddleware': 543,
}
