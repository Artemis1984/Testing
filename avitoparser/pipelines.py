# -*- coding: utf-8 -*-

from pprint import pprint

from scrapy.pipelines.images import ImagesPipeline
import scrapy

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class AvitoparserPipeline(object):

    def process_item(self, item, spider):

        temp_dict = {'Название': item['name'][0],
                     'Фото': item['photos'],
                     'Цена': item['price'],
                     'Источник': spider.name}

        if item['params_keys']:
            for i in range(len(item['params_keys'])):
                temp_dict[item['params_keys'][i]] = item['params_values'][i].replace(' ', '').replace('\xa0', '')

        pprint(temp_dict)

        return item


class AvitoPhotosPipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        if item['photos']:
            for img in item['photos']:
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)

    def item_completed(self, results, item, info):

        if results:

            item['photos'] = [itm[1] for itm in results if itm[0]]

            images = open('images' + item, 'a')

            for i in item:
                images.write('images' + item['name'])


        return item
