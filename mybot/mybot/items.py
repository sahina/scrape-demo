# -*- coding: utf-8 -*-
from scrapy import Field, Item


class CountryItem(Item):
    country_name = Field()
    url = Field()

class CountryDetailItem(Item):
    country_detail_name = Field()

class TeamItem(Item):
    team_name = Field()
