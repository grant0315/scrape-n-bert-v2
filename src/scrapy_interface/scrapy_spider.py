import scrapy
import src.helpers.common as com
from scrapy.crawler import CrawlerProcess

class SNBSpider(scrapy.Spider):

    def __init__(self, *args, **kwargs):
        self.links = []
        self.css_selector = kwargs.get('css_sel')
        
        self.name = 'all'
        self.start_urls = [kwargs.get('urls')]
        self.allowed_domains = [com.remove_scheme_from_url(kwargs.get('urls'))]

    # Don't look at me that way. Stupid recursion problems.
    def parse(self, response):
        self.links.append(response.url)
        for resp in response.css(self.css_selector):
            data = { "content" : resp.get(),
                        "url" : response.request.url }
            yield data

        for href in response.css('a::attr(href)'):
            yield response.follow(href, self.parse)

def start_scrape(urls, css_selector, total_page_count, output_directory, output_filename):
    process = CrawlerProcess(settings={
    "REDIRECT_MAX_TIMES" : 5,
    "CLOSESPIDER_PAGECOUNT" : total_page_count,
    "DNS_TIMEOUT": 10,
    "SPIDER_MIDDLEWARES": {
        "scrapy.spidermiddlewares.offsite.OffsiteMiddleware": True,
        },
    "FEED_FORMAT": "json",
    "FEED_URI": str(output_directory + "/" + output_filename + ".json"),
    })

    process.crawl(SNBSpider, css_sel=css_selector, urls=urls)
    process.start()