# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import newscrawler.CustomMiddleware
import os
import json
import codecs
import pymongo
from newscrawler.items import NewsItem,CommentItem
class NewsPipline(object):

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'items')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):

        if isinstance(item, NewsItem):
            collection_name = 'news_table'
            self.db[collection_name].insert_one(dict(item))
        elif isinstance(item, CommentItem):
            collection_name = 'comments'
            self.db[collection_name].insert_one(dict(item))


        return item




#
#
# class NewscrawlerPipeline(object):
#     def __init__(self):
#         self.current_dir = os.getcwd()
#
#     def process_item(self, item, spider):
#         dir_path = self.current_dir + '/docs/' + item['source'] + '/' + item['date']
#         if not os.path.exists(dir_path):
#             os.makedirs(dir_path)
#
#         news_file_path = dir_path + '/' + item['newsId'] + '.json'
#         if os.path.exists(news_file_path) and os.path.isfile(news_file_path):
#             print('---------------------------------------')
#             print(item['newsId'] + '.json exists, not overriden')
#             print('---------------------------------------')
#             return item
#
#         news_file = codecs.open(news_file_path, 'w', 'utf-8')
#         line = json.dumps(dict(item))
#         news_file.write(line)
#         news_file.close()
#
#         txt_dir_path = self.current_dir + '/txts/' + item['source'] + '/' + item['date']
#         if not os.path.exists(txt_dir_path):
#             os.makedirs(txt_dir_path)
#
#         news_txt_path = txt_dir_path + '/' + item['newsId'] + '.txt'
#         if os.path.exists(news_txt_path) and os.path.isfile(news_txt_path):
#             print('|||||||||||||||||||||||||||||||||||||||')
#             print(item['newsId'] + '.json exists, not overriden')
#             print('|||||||||||||||||||||||||||||||||||||||')
#             return item
#
#         with open(news_txt_path, mode='w', encoding='utf-8') as f:
#             # content = json.loads(item['contents'])
#             raw = [item['contents']['title'],item['contents']['passage']]
#             f.writelines(raw)
#
#
#         return item
