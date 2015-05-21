from scrapy import Field, Item
from scrapy.contrib.loader import ItemLoader
from scrapy.contrib.loader.processor import TakeFirst


class CountryItem(Item):
    item = Field()
    country_name = Field()
    country_flag_url1 = Field()
    country_flag_url2 = Field()
    country_flag_url3 = Field()
    country_flag_url4 = Field()
    country_flag_url5 = Field()
    confederation_alias = Field()
    association_url = Field()


class CountryLoader(ItemLoader):
    default_output_processor = TakeFirst()


class AssociationItem(Item):
    item = Field()
    country_name = Field()
    country_flag_url1 = Field()
    country_flag_url2 = Field()
    country_flag_url3 = Field()
    country_flag_url4 = Field()
    country_flag_url5 = Field()
    league_name = Field()
    league_id = Field()
    league_logo_url_s = Field()
    league_logo_url_m = Field()
    standings_url = Field()


class AssociationLoader(ItemLoader):
    default_output_processor = TakeFirst()


class StandingsItem(Item):
    item = Field()
    league_id = Field()
    club_name = Field()
    club_id = Field()
    club_url = Field()


class StandingsLoader(ItemLoader):
    default_output_processor = TakeFirst()
