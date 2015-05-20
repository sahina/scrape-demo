# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mybot.items import CountryItem, TeamItem


class ServerSpider(CrawlSpider):
    name = "server"
    allowed_domains = ["localhost"]
    start_urls = [
        'http://localhost:8080/index.html'
    ]

    rules = [
        Rule(LinkExtractor(allow='countries\.html'), callback='parse_countries', follow=True),
        Rule(LinkExtractor(allow='c-.*\.html'), callback='parse_country', follow=True)
    ]

    def parse_country(self, response):
        print 'parse_country >>> {0} ***************'.format(response.url)
        for c in response.xpath("//li"):
            item = TeamItem()
            item["name"] = c.xpath("./text()").extract()

            yield item


    def parse_countries(self, response):
        print 'parse_countries >>>  {0} ***************'.format(response.url)
        for c in response.xpath("//a[@class='country-link']"):
            item = CountryItem()
            item["name"] = c.xpath('./text()').extract()
            item["url"] = c.xpath('./@href').extract()

            yield item
        
