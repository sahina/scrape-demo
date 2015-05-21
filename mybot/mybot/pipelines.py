# -*- coding: utf-8 -*-
import re


class StandingsPipeline(object):
    def process_item(self, item, spider):
        if 'club_url' in item:
            m = re.search('(?:\d)?\d+', item['club_url'])
            club_id = m.group(0)
            if club_id:
                item['club_id'] = club_id

        return item


class TestPipeline(object):
    def process_item(self, item, spider):
        print 'test pipeline'

        return item
