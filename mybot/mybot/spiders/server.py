# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor


class ServerSpider(CrawlSpider):
    name = "server"
    allowed_domains = ["localhost"]
    start_urls = [
        'http://localhost:8080/index.html'
    ]

    rules = [
        Rule(LinkExtractor(allow='.*'), follow=True, callback='parse_links')
    ]

    def parse_links(self, response):
        print '>>> parse_links'

