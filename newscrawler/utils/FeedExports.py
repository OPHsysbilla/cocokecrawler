import datetime
import os
import json
import codecs
import newscrawler.utils.configure as cfg
from newscrawler.items import CommentItem,NewsItem

# 根据json生成Comment
def genaCommentItem(dictC):
    # http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/CSBMN1GN0001875P/comments/newList?offset=0&limit=30&showLevelThreshold=72&headLimit=1&tailLimit=2&callback=getData&ibc=newspc&_=1503375536399
    # 保留需要内容

    dicSample = {
                  'docId': 'xxxxx',
                  'against': 0,
                  'content': '可能这家米粉店就是他们局承包经营的，人人有份，能从中分到好处，自然也就不会管。',
                  'createTime': '2017-08-20 07:13:44',
                   'location': '广东省汕头市',
                   'nickname': '庆东', # 可能是匿名，没有名字
                   'vote': 1}

    # 只保留筛选需要的信息
    # 如dicSample的格式
    itemList = []
    comment = dictC['comments']
    for userId in comment:
        item = CommentItem()
        item['docId'] = dictC['docId']
        item['against'] = comment[userId]['against']
        item['content'] = comment[userId]['content']
        item['createTime'] = comment[userId]['createTime']
        item['vote'] = comment[userId]['vote']

        user = comment[userId]['user']
        item['location'] = user['location']
        item['nickname'] = user['nickname']  if 'nickname' in user else '匿名'
        itemList.append(item)
    return itemList

    # # 读取信息传递
    # docId = dictC['docId']
    # offset = dictC['offset']

    # 保存listSave
    # SaveCommentListJson(listSave,docId=docId,offset=offset)

def SaveCommentListJson(listSave,docId,offset):
    nowTime = datetime.datetime.now()
    # 根据时间来安排文件夹名
    datestr = "%04d%02d%02d" % (nowTime.year, nowTime.month, nowTime.day)
    # 文件夹存放
    comment_dir = cfg.SAVE_COMMENT_DIR

    # 文件地址
    json_dir_path = comment_dir + '/' + datestr + '/' + docId
    if not os.path.exists(json_dir_path):
        os.makedirs(json_dir_path)

    # 文件名
    comments_json_path = json_dir_path \
                         + '/offset-' + offset  +'.json'
    if os.path.exists(comments_json_path) and os.path.isfile(comments_json_path):
        print('/'*15)
        print(datestr + '/' +docId + '/offset-' + offset  +'.json' + '.json exists, not overriden')
        print('/'*15)

    # 写入
    with codecs.open(comments_json_path, mode='w', encoding='utf-8') as f:
        line = json.dumps(listSave)
        f.write(line)

# # 看文章是否存在在news_table中,只能看news的
# def ifExistsInDB(docId):
#     import pymongo
#     try:
#         client = pymongo.MongoClient('mongodb://localhost:27017/')
#         tb = client['cocoke']['news_table']
#         client.close()
#         return tb.find_one({"docId": docId}) != None
#
#     except IOError as e:
#         print("ifExistsInDB",e)
#         pass




# 给标准新闻使用
def makeNewsItem(url, docId, title, createTime, content, source):
    item = NewsItem()
    item['url'] = url
    item['docId'] = docId
    item['title'] = title
    item['createTime'] = createTime
    item['content'] = content
    item['source'] = source
    return item

# 给json格式新闻使用
def genaNewsItem(dicN):
    # 保留需要内容
    dicSample = {
        "url":"http:xxxxx",
        "docId":'xxxxx',
        "title": "广州今年还有3条地铁开工 周边房价地图奉上",
        "createTime": "2017-08-18 17:15:50",
        "content": "根据地铁官方公布，18、22、11号线将有望于年内全面开工，其中18、22号线涉及南沙与中心区的联系，11号线为广州首条“市区环线”。这个图集将为大家带来地铁房价地图以及简要的规划利好分析。（数据来源：中原研究发展部）",
        "source": ""
    }

    # 只保留筛选需要的信息
    # 如dicSample的格式
    item = NewsItem()
    info = dicN['info']
    item['url'] = dicN['url']
    item['docId'] = dicN['docId']
    item['title'] = info['setname']
    item['createTime'] = info['lmodify']
    item['content'] = dicN['content']
    item['source'] = info['source']

    return item
    # SaveNewsJson(dicSave=item)
    # 保存listSave


def SaveNewsJson(dicSave):
    nowTime = datetime.datetime.now()
    # 根据时间来安排文件夹名
    datestr = "%04d%02d%02d" % (nowTime.year, nowTime.month, nowTime.day)
    # 文件夹存放
    dir = cfg.SAVE_COMMENT_DIR

    docId = dicSave['docId']
    # 文件地址
    json_dir_path = dir + '/'  + datestr + '/' + docId
    if not os.path.exists(json_dir_path):
        os.makedirs(json_dir_path)

    # 文件名
    json_path = json_dir_path \
                         +'/main.json'
    if os.path.exists(json_path) and os.path.isfile(json_path):
        print('/'*15)
        print( datestr + '/' + docId + '/main.json exists, not overriden')
        print('/'*15)

    # 写入
    with codecs.open(json_path, mode='w', encoding='utf-8') as f:
        line = json.dumps(dicSave)
        f.write(line)
