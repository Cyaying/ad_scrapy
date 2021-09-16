# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AdScrapyItem(scrapy.Item):
    category = scrapy.Field()
    title = scrapy.Field()
    abstract = scrapy.Field()
    url = scrapy.Field()
    nickname = scrapy.Field()
    views = scrapy.Field()
