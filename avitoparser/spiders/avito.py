# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import HtmlResponse
from avitoparser.items import AvitoparserItem
from scrapy.loader import ItemLoader


class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/rossiya']

    def __init__(self, section):
        super(AvitoSpider, self).__init__()
        self.start_urls = [f'https://www.avito.ru/rossiya/{section}?q=1']

    def parse(self, response: HtmlResponse):

        add_link = response.xpath("//a[@class= 'snippet-link']/@href").extract()

        for link in add_link:

            yield response.follow(link, callback=self.parse_add)

    def parse_add(self, response: HtmlResponse):

        loader = ItemLoader(item=AvitoparserItem(), response=response)
        loader.add_xpath('name', "//span[@class= 'title-info-title-text']/text()")
        loader.add_xpath('price', "//span[@class= 'js-item-price']/text()")
        loader.add_xpath('photos', "//div[@class= 'gallery-img-wrapper js-gallery-img-wrapper']/div/@data-url")

        if response.xpath("//div[@class= 'item-params']"):
            loader.add_xpath('params_keys', "//ul[@class= 'item-params-list']/li//span/text()")
            loader.add_xpath('params_values', "//ul[@class= 'item-params-list']/li/text()")

            # print('params')

        else:
            loader.add_value('params_keys', 'Параметры: ')
            loader.add_value('params_values', 'Отсутствуют')

        yield loader.load_item()
