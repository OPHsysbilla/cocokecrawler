
from newscrawler.items import NewsItem

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import Selector
import re
import json

from newscrawler.utils.FeedExports import genaCommentItem,genaNewsItem,makeNewsItem

from newscrawler.utils.polishString import reFind,reFindAllHref,stripToJSFormat,howToExtractContent,strfind,findKeyWordJson,extractLabelP,typeNews,concateCommentApi \
    ,extractTextArea,extractTime,getAttributeFromUrl

from scrapy import Spider,Request

import scrapy.utils.defer
class NormalCommentSpider(Spider):

    name = "normal_comment_spider"
    allowed_domains = ['163.com']

    start_urls =[
         'http://news.163.com/special/0001386F/rank_whole.html',
         # 'http://news.163.com/special/0001386F/rank_news.html',
         # 'http://news.163.com/special/0001386F/rank_ent.html',
         # 'http://news.163.com/special/0001386F/rank_sports.html'  ,
         # 'http://money.163.com/special/002526BH/rank.html',
         # 'http://news.163.com/special/0001386F/rank_tech.html',
         # 'http://news.163.com/special/0001386F/rank_auto.html',
         # 'http://news.163.com/special/0001386F/rank_lady.html',
         # 'http://news.163.com/special/0001386F/rank_house.html',
         # 'http://news.163.com/special/0001386F/rank_book.html',
         # 'http://news.163.com/special/0001386F/game_rank.html',
         # 'http://news.163.com/special/0001386F/rank_travel.html',
         # 'http://news.163.com/special/0001386F/rank_edu.html',
         # 'http://news.163.com/special/0001386F/rank_gongyi.html',
         # 'http://news.163.com/special/0001386F/rank_campus.html',
         # 'http://news.163.com/special/0001386F/rank_media.html',
         # 'http://news.163.com/special/0001386F/rank_video.html',
        ]

    # rules = [Rule(LxmlLinkExtractor(allow=[url_pattern]), callback='parse_news', follow=True)]
    """ 分析评论 
        所有进来的页面都只可能是评论，分析docId是新闻正文干的事
    """
    def parse_comment(self,response):
        try:
            # scrip_content怎么解决？scrip_content是指从新闻到评论需要
            whichType = howToExtractContent(response.url)
            if whichType == typeNews['comment']:
                # 此时链接地址上有offset，读取即可
                # offset后面需要加减
                offset = int(getAttributeFromUrl(url=response.url,keyword='offset'))
                # docId 不需要，就是str
                docId = getAttributeFromUrl(url=response.url, keyword='docId')

                # offset增加，继续抓取评论，直到遇到报错
                ListType = 'hotList' if response.url.find('hotList') else 'newList'
                OFFSET_CONST = 30 if ListType == 'newList' else 40
                productKey = getAttributeFromUrl(url=response.url, keyword='productKey')

                # 保存得到jsoncomment
                # 去掉开头的getData( 和末尾的);
                body = str(response.body, encoding="utf-8")
                comment_json = stripToJSFormat(body)
                dictCommentOFFSET = json.loads(comment_json)

                # 处理api：[illegal和超出上限情况]，由于评论还在不断增加，所以无法根据newListSize来判断
                # 只有两种情况：字典为空 或者 code 报错
                # (即 comments这个键 为空或不存在)
                # dicta = {"commentIds":[],"comments":{},"newListSize":9371}
                # dictb = {"code":"42212","message":"Illegal pagination parameters"}

                # 字典为空
                if not dictCommentOFFSET["comments"]:
                    raise EOFError("现在已到评论最底部")
                # 记录docId
                dictCommentOFFSET['docId'] = docId

                # 请求新url前先看是否已经存在了offset(不完成)

                # 请求新评论url
                header = {'Host': 'comment.news.163.com',
                          'Accept': '*/*',
                          'Referer': response.url,
                          'Accept-Encoding': 'gzip, deflate',
                          'Accept-Language': 'zh-CN,zh;q=0.8'}
                new_url = concateCommentApi( productKey=productKey,
                                             docId=docId,
                                             offset= str(offset + OFFSET_CONST),
                                             ListType='newList')
                print('docId',docId,"offset:",offset+OFFSET_CONST)
                yield Request(url=new_url, callback=self.parse_comment,priority=0)

                # 生成Item
                ItemList = genaCommentItem(dictCommentOFFSET)
                for commentItem in ItemList:
                    yield commentItem


        except Exception as e:
            print('in comment',e)
            pass
    # def make_requests_from_url(self,url):
    #
    #     return Request(url, dont_filter=True)

    def parse(self, response):
        tabContents = response.css('.tabContents')
        for url in reFindAllHref(tabContents):
            if url is not None:
                header = {'Host':'news.163.com',
                        'Accept': '*/*',
                        'Referer': response.url,
                        'Accept-Encoding': 'gzip, deflate',
                        'Accept-Language': 'zh-CN,zh;q=0.8'}
                yield Request(url=url, callback=self.parse_new ,priority=5,
                              headers=header)



    """ 根据不同的类型提取新闻正文 """
    def parse_new(self, response):
        self.log('in parse_new')

        # try:
        NewsUrl = response.url
        # 新闻链接类型
        whichType = howToExtractContent(NewsUrl)
        # 准备所需信息
        scrip_content = self.getScriptText(response)
        docId = findKeyWordJson(html_content=scrip_content
                                , keyword='docId')
        productKey = findKeyWordJson(html_content=scrip_content
                                     , keyword='productKey')
        # print(docId)
        # print(productKey)
        # 分析评论Api的第一页
        # 需要在script中查找docId
        # 提取 "docId"
        new_url = concateCommentApi(productKey=productKey,
                                    docId=docId,
                                    offset='0',
                                    ListType='newList')
        header = {'Host': 'comment.news.163.com',
                  'Accept': '*/*',
                  'Referer': response.url,
                  'Accept-Encoding': 'gzip, deflate',
                  'Accept-Language': 'zh-CN,zh;q=0.8'}
        yield Request(url=new_url, callback=self.parse_comment,priority=1)



        # 标准新闻链接
        if whichType == typeNews['news']:
            # 抽取内容
            EndText = response.css('#endText').extract()
            content = extractLabelP(EndText)
            # 抽取其他
            title = response.css('h1::text').extract_first()
            timee = response.css('.post_time_source::text').extract_first()
            source = response.css('.post_time_source>a::text').extract_first()
            creatTime = extractTime(timee)
            newsItem = makeNewsItem(url=NewsUrl,
                                docId=docId,
                                title=title,
                                createTime=creatTime,
                                content=content,
                                source=source)
            # 生成
            yield newsItem

        # 网易号 ,新闻正文在id = content中
        elif whichType == typeNews['dy']:
            EndText = response.css('#content').extract()
            content = extractLabelP(EndText)
            # 抽取其他
            title = response.css('h2::text').extract_first().strip()
            source = '网易号'
            creatTime = response.css('.time>span::text').extract_first()
            newsItem = makeNewsItem(url=NewsUrl,
                                docId=docId,
                                title=title,
                                createTime=creatTime,
                                content=content,
                                source=source)
            # 保存
            yield newsItem

        # 图集，是读取textArea内的内容
        # others可以不管正文，一般是直播之类的
        elif whichType == typeNews['photoview'] or whichType == typeNews['others']:
            # 尝试读取textArea
            textAreaLabel = response.css('textarea::text').extract()
            if textAreaLabel:
                # 提取textArea内文本
                nexturls, textAreaDic = extractTextArea(textAreaLabel)

                # 保存读取的信息
                textAreaDic['docId'] = docId
                textAreaDic['url'] = NewsUrl
                newsItem = genaNewsItem(textAreaDic)
                yield newsItem

                # 读取下一个链接
                for url in nexturls:
                    yield Request(url=url, callback=self.parse_new,priority=5)
        # except Exception as e:
        #     print("parse_new",e)
        #     pass

    def getScriptText(self,response):
        scrip = response.css('script').extract()
        scrip_content = "".join(scrip)
        return scrip_content
