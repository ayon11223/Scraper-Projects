# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CountryinfoItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    capital = scrapy.Field()
    population = scrapy.Field()
    area = scrapy.Field()
