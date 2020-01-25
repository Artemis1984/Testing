# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy.loader.processors import TakeFirst, MapCompose

import scrapy


def int_price(value):

    try:
        return int(str(value).replace(' ', ''))
    except Exception:
        return 'Не указано'


def photo_link(link):

    return 'https:' + link


def make_params(params: list):

    if params:

        if params == 'Не указано':

            return params

        if params == ' ':

            return
        else:
            return params
    else:
        return


class AvitoparserItem(scrapy.Item):
    # define the fields for your item here like:

    # name = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field()
    photos = scrapy.Field(input_processor=MapCompose(photo_link))
    price = scrapy.Field(output_processor=TakeFirst(), input_processor=MapCompose(int_price))
    params_keys = scrapy.Field()
    params_values = scrapy.Field(input_processor=MapCompose(make_params))
