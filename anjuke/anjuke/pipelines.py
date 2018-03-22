# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.pipelines.images import ImagesPipeline

class Day14Pipeline(object):
    def process_item(self, item, spider):
        return item

class HouseImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        print(results)
        return item