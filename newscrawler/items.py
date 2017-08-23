# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field

# dicSample = {
#     'docId': 'xxxxx',
#     'against': 0,
#     'content': '可能这家米粉店就是他们局承包经营的，人人有份，能从中分到好处，自然也就不会管。',
#     'createTime': '2017-08-20 07:13:44',
#     'location': '广东省汕头市',
#     'nickname': '庆东',  # 可能是匿名，没有名字
#     'vote': 1}


class CommentItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    docId = Field()
    against = Field()
    content = Field()
    createTime = Field()
    location = Field()
    nickname = Field()
    vote = Field()

    def __str__(self):
        return "comment downloading ...  "


class NewsItem(Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = Field()
    docId = Field()
    title = Field()
    createTime = Field()
    content = Field()
    source = Field()

    def __str__(self):
        return "news downloading ...  "

# dicSample = {
#         "url":"http:xxxxx",
#         "docId":'xxxxx',
#         "title": "广州今年还有3条地铁开工 周边房价地图奉上",
#         "createTime": "2017-08-18 17:15:50",
#         "content": "根据地铁官方公布，18、22、11号线将有望于年内全面开工，其中18、22号线涉及南沙与中心区的联系，11号线为广州首条“市区环线”。这个图集将为大家带来地铁房价地图以及简要的规划利好分析。（数据来源：中原研究发展部）",
#         "source": ""
#     }