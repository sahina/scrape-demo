# -*- coding: utf-8 -*-
import scrapy


class ServerSpider(scrapy.Spider):
    name = "server"
    allowed_domains = ["localhost:8090"]
    start_urls = (
        'http://localhost:8090',
    )

    def parse(self, response):
        pass
