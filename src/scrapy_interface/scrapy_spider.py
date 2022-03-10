import scrapy
import json
import urllib
from scrapy import signals
import src.helpers.common as com
from scrapy.crawler import CrawlerProcess

class SNBSpider(scrapy.Spider):

    def __init__(self, *args, **kwargs):
        self.links = []
        self.css_selector = kwargs.get('css_sel')

        self.name = 'signals'
        self.start_urls = [kwargs.get('urls')]
        self.allowed_domains = [com.remove_scheme_from_url(kwargs.get('urls'))]


    # Don't look at me that way. Stupid recursion problems.
    def parse(self, response):
        for content in response.css(self.css_selector):
            yield { 'url': response.url, 'content': content.extract() }
        
        for next_page in response.css("a::attr(href)"):
            if next_page is not None:
                yield response.follow(next_page, self.parse)

    def parse_dir_contents(self, response):
        for sel in response.css(self.css_selector):
            item = {}
            item['url'] = response.url
            item['content'] = sel.extract()
            yield item

def start_scrape(urls, css_selector, total_page_count, depth_limit, output_directory, output_filename):
    process = CrawlerProcess(settings={
    "REDIRECT_MAX_TIMES" : 5,
    "CLOSESPIDER_PAGECOUNT" : total_page_count,
    "DEPTH_LIMIT": depth_limit,
    "DNS_TIMEOUT": 10,
    "SPIDER_MIDDLEWARES": {
        "scrapy.spidermiddlewares.offsite.OffsiteMiddleware": True,
        },
    "FEED_FORMAT": "csv",
    "FEED_URI": str(output_directory + "/" + output_filename + ".csv"),
    })

    process.crawl(SNBSpider, css_sel=css_selector, urls=urls)
    process.start()
    


