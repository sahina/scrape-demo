# -*- coding: utf-8 -*-
import os

BOT_NAME = 'mybot'

SPIDER_MODULES = ['mybot.spiders']
NEWSPIDER_MODULE = 'mybot.spiders'

ITEM_PIPELINES = {
    'mybot.pipelines.StandingsPipeline': 400,
    'mybot.pipelines.CountryFlagPipeline': 200,
    'mybot.pipelines.LeagueLogoPipeline': 500,
    'mybot.pipelines.FifaImagesPipeline': 600
}

CUR_DIR = os.path.dirname(os.path.realpath(__file__))
IMAGES_STORE = os.path.join(CUR_DIR, 'fifa-img')

DOWNLOAD_DELAY = 0.25

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'uefa (+http://www.uefa.com)'
