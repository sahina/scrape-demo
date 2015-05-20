# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mybot.items import CountryItem, CountryDetailItem, TeamItem


class ServerSpider(CrawlSpider):
    name = "server"
    allowed_domains = ["localhost"]
    start_urls = [
        'http://localhost:8080/index.html'
    ]

    rules = [
        Rule(LinkExtractor(allow='countries\.html'), callback='parse_countries', follow=True),
        Rule(LinkExtractor(allow='c-.*\.html'), callback='parse_country', follow=True),
        Rule(LinkExtractor(allow='x-.*\.html'), callback='parse_country_details', follow=True)
    ]

    def parse_country(self, response):
        print 'parse_country >>> {0} ***************'.format(response.url)

        for c in response.xpath("//a[@class='country-item']"):
            item = TeamItem()
            item["team_name"] = c.xpath("./text()").extract()

            yield item


    def parse_countries(self, response):
        print 'parse_countries >>>  {0} ***************'.format(response.url)

        for c in response.xpath("//a[@class='country-link']"):
            item = CountryItem()
            item["country_name"] = c.xpath('./text()').extract()
            item["url"] = c.xpath('./@href').extract()

            yield item
        
    def parse_country_details(self, response):
        print 'parse_country_details >>>  {0} ***************'.format(response.url)

        item = CountryDetailItem()
        item["country_detail_name"] = response.xpath("//h1/text()").extract()

        yield item
