# -*- coding: utf-8 -*-
from scrapy import Field, Item


class CountryItem(Item):
    name = Field()
    url = Field()

class TeamItem(Item):
    name = Field()
