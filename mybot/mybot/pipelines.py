# -*- coding: utf-8 -*-
import re
from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy import Request


class StandingsPipeline(object):
    def process_item(self, item, spider):
        if 'club_url' in item and item['item'] == 'standings':
            m = re.search('(?:\d)?\d+', item['club_url'])
            club_id = m.group(0)
            if club_id:
                item['club_id'] = club_id

        return item


class CountryFlagPipeline(object):
    def process_item(self, item, spider):
        if 'country_flag_url3' in item:
            item['country_flag_url1'] = item['country_flag_url3'].replace('flags/3/', 'flags/1/')
            item['country_flag_url2'] = item['country_flag_url3'].replace('flags/3/', 'flags/2/')
            item['country_flag_url4'] = item['country_flag_url3'].replace('flags/3/', 'flags/4/')
            item['country_flag_url5'] = item['country_flag_url3'].replace('flags/3/', 'flags/5/')

            item['image_urls'] = []
            item['image_urls'].append(item['country_flag_url1'])
            item['image_urls'].append(item['country_flag_url2'])
            item['image_urls'].append(item['country_flag_url3'])
            item['image_urls'].append(item['country_flag_url4'])
            item['image_urls'].append(item['country_flag_url5'])

        return item


class LeagueLogoPipeline(object):
    def process_item(self, item, spider):
        if 'league_logo_url_s' in item:
            item['league_logo_url_m'] = item['league_logo_url_s'].replace('logos/s/', 'logos/m/')

            item['image_urls'] = []
            item['image_urls'].append(item['league_logo_url_s'])
            item['image_urls'].append(item['league_logo_url_m'])
        return item


class FifaImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if 'image_urls' in item:
            for image_url in item['image_urls']:
                yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        item['image_paths'] = image_paths
        return item
