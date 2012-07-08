# Scrapy settings for livingsocial_crawler project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'livingsocial_crawler'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['livingsocial_crawler.spiders']
NEWSPIDER_MODULE = 'livingsocial_crawler.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

ITEM_PIPELINES = ['livingsocial_crawler.pipelines.AlcoholPipeline']

