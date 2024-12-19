# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlogdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class BlogData(scrapy.Item):
    title: scrapy.Field()
    detail: scrapy.Field()
    content: scrapy.Field()  # type: ignore
    link: scrapy.Field()
