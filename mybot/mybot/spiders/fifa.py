from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from mybot.items import CountryItem, CountryLoader, AssociationItem, AssociationLoader, TeamItem


class ServerSpider(CrawlSpider):
    name = "fifa"
    allowed_domains = ["fifa.com"]
    start_urls = [
        'http://fifa.com'
    ]

    rules = [
        Rule(LinkExtractor(allow='associations\/index\.html', restrict_xpaths="//*[@id='mitem-associations']/a"),
             callback='parse_countries', follow=True),
        Rule(LinkExtractor(allow='c-.*\.html'),
             callback='parse_associations', follow=True),
        # Rule(LinkExtractor(allow='x-.*\.html'), callback='parse_country_details', follow=True)
    ]

    def parse_countries(self, response):
        print '*************** parse_countries >>>  {0} ***************'.format(response.url)

        for a in response.xpath("//li[@data-confederation]"):
            l = CountryLoader(item=CountryItem(), response=response)

            l.add_value('country_name', a.xpath(".//span[@class]/text()").extract())
            l.add_value('country_flag_url3', a.xpath("./a/img/@src").extract())
            l.add_value('confederation_alias', a.xpath("./@data-confederation").extract())
            l.add_value('association_url', a.xpath("./a/@href").extract())

            yield l.load_item()

    def parse_associations(self, response):
        print 'parse_country >>> {0} ***************'.format(response.url)

        for c in response.xpath("//a[@class='country-item']"):
            item = TeamItem()
            item["team_name"] = c.xpath("./text()").extract()

            yield item

    def parse_country_details(self, response):
        print 'parse_country_details >>>  {0} ***************'.format(response.url)

        item = AssociationItem()
        item["country_detail_name"] = response.xpath("//h1/text()").extract()

        yield item
