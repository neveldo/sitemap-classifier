from datetime import datetime
from scrapy.spiders import SitemapSpider
from smclassifier.scraping import settings

class ArticlesSpider(SitemapSpider):

    name = "articles"

    allowed_domains = settings.ALLOWED_DOMAINS
    sitemap_urls = settings.SITEMAP_URLS

    sitemap_rules = [
        (r'\d+$', 'parse_article'),
    ]

    def sitemap_filter(self, entries):
        for entry in entries:
            date_time = datetime.strptime(entry['lastmod'][0:10], '%Y-%m-%d')
            if date_time.year >= 2015:
                yield entry

    def parse_article(self, response):
        yield {
            'url': response.url,
            'lastmod': response.css('header time::attr(datetime)').get(),
            'title': response.css('h1::text').get(),
            'article': str(response.css('#article-detail').get()),
        }
