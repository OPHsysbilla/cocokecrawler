import re
def test():
    url = 'http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/CSBMN1GN0001875P/comments/newList?offset=0&limit=30&showLevelThreshold=72&headLimit=1&tailLimit=2&callback=getData&ibc=newspc&_=1503336410452'
    keyword = 'limit'
    pattern = keyword+'=([^=]+)(?=&)'
    print(re.findall(pattern=pattern,string=url))
    print(re.search(pattern=pattern,string=url).group(1))

if __name__=='__main__':
    string = '"productKey": "a2869674571f77b5a0867c3d71db5856", //"a2869674571f77b5a0867c3d71db5856",\
            "docId": "CSDBEOI105239C5S",'
    keyword = 'docId'
    pattern = '"' + keyword + '"\s*:\s*"([^"]*?)"'
    print(re.findall(string=string, pattern=pattern))



    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
        "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
        "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
        "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.11 TaoBrowser/2.0 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 LBBROWSER",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
        "Mozilla/5.0 (iPad; U; CPU OS 4_2_1 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8C148 Safari/6533.18.5",
        "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0b13pre) Gecko/20110307 Firefox/4.0b13pre",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:16.0) Gecko/20100101 Firefox/16.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11",
        "Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",

    ]

    s2=set(user_agent_list)
    # print(len(user_agent_list),len(s2))
    # print(list(s2))
    # 字符串->时间转换
    import time
    res = time.strptime('2017-08-22 17:39:54', "%Y-%m-%d %H:%M:%S")

    # def ifExistsInDB(docId):
    #     import pymongo
    #     try:
    #         client = pymongo.MongoClient('mongodb://localhost:27017/')
    #         tb = client['cocoke']['news_table']
    #         client.close()
    #         return tb.find_one({"docId": docId})!=None
    #
    #     except IOError as e:
    #         print(e)
    #         pass
    #
    # print(ifExistsInDB('sda'))
    # print(ifExistsInDB('CSDF40II00088570'))


            #
#
#
# class crawlCommentSpider(CrawlSpider):
#     name = 'crawl_comment_spider'
#     allowed_domains = ['163.com']
#     start_urls = ['http://news.163.com/special/0001386F/rank_whole.html']
#     url_pattern = r'(http://.*?\.sohu\.com)/(\d{8})/(\w+)\.shtml'
#     rules = [
#         Rule(LxmlLinkExtractor(allow=[r'http://\S+\.163\.com/\d{2}/\d{4}/\d+/\w+\.html']),
#              callback='parse_news', follow=False),
#         Rule(LxmlLinkExtractor(allow=[r'\A(.+article/detail.+)\Z']),
#          callback='parse_dy', follow=False),
#         Rule(LxmlLinkExtractor(allow=[r'\A(.+photo[view|new].+)\Z']),
#             callback='parse_others', follow=False),
#         Rule(LxmlLinkExtractor(allow=[r'\A(comment.news.163.com/api/v1/products.+)\Z']),
#              callback='parse_comment', follow=False)
#
#     ]
#
#     # process_links
#     # 是一个callable或string(该spider中同名的函数将会被调用)。 从link_extractor中获取到链接列表时将会调用该函数。该方法主要用来过滤。
#     #
#     # process_request
#     # 是一个callable或string(该spider中同名的函数将会被调用)。 该规则提取到每个request时都会调用该函数。该函数必须返回一个request或者None。 (用来过滤request)
#
#     # # 可以处理提取到的地址
#     # def process_value(value):
#     #     m = re.search("javascript:goToPage\('(.*?)'", value)
#     #     if m:
#     #         return m.group(1)
#
#     def parse_start_url(self,response):
#         tabContents = response.css('.tabContents')
#         for url in reFindAllHref(tabContents):
#             if url is not None:
#                 header = {'Host':'news.163.com',
#                         'Accept': '*/*',
#                         'Referer': response.url,
#                         'Accept-Encoding': 'gzip, deflate',
#                         'Accept-Language': 'zh-CN,zh;q=0.8'}
#                 yield Request(url=url, callback=self.parse_new)
#
#                 # rules = [Rule(LxmlLinkExtractor(allow=[url_pattern]), callback='parse_news', follow=True)]
#
#
#     def parse_comment(self, response):
#         try:
#             # scrip_content怎么解决？scrip_content是指从新闻到评论需要
#             whichType = howToExtractContent(response.url)
#             if whichType == typeNews['comment']:
#                 # 此时链接地址上有offset，读取即可
#                 # offset后面需要加减
#                 offset = int(getAttributeFromUrl(url=response.url,keyword='offset'))
#                 # docId 不需要，就是str
#                 docId = getAttributeFromUrl(url=response.url, keyword='docId')
#                 # 保存得到jsoncomment
#                 # 去掉开头的getData( 和末尾的);
#                 body = str(response.body, encoding="utf-8")
#                 comment_json = stripToJSFormat(body)
#                 dictCommentOFFSET = json.loads(comment_json)
#
#                 # 处理api：[illegal和超出上限情况]，由于评论还在不断增加，所以无法根据newListSize来判断
#                 # 只有两种情况：字典为空 或者 code 报错
#                 # (即 comments这个键 为空或不存在)
#                 # dicta = {"commentIds":[],"comments":{},"newListSize":9371}
#                 # dictb = {"code":"42212","message":"Illegal pagination parameters"}
#
#                 # 字典为空
#                 if not dictCommentOFFSET["comments"]:
#                     raise EOFError("现在已到评论最底部")
#                 # 记录docId
#                 dictCommentOFFSET['docId'] = docId
#                 # 生成Item
#                 ItemList = genaCommentItem(dictCommentOFFSET)
#                 for commentItem in ItemList:
#                     yield commentItem
#
#                 # offset增加，继续抓取评论，直到遇到报错
#                 ListType = 'hotList' if response.url.find('hotList') else 'newList'
#                 OFFSET_CONST = 30 if ListType == 'newList' else 40
#                 productKey = getAttributeFromUrl(url=response.url,keyword='productKey')
#
#                 # 请求新url前先看是否已经存在了offset(不完成)
#
#                 # 请求新评论url
#                 header = {'Host': 'comment.news.163.com',
#                           'Accept': '*/*',
#                           'Referer': response.url,
#                           'Accept-Encoding': 'gzip, deflate',
#                           'Accept-Language': 'zh-CN,zh;q=0.8'}
#                 new_url = concateCommentApi( productKey=productKey,
#                                              docId=docId,
#                                              offset= str(offset + OFFSET_CONST),
#                                              ListType='newList')
#                 yield response.urljoin(url=new_url, callback=self.parse_comment)
#         except Exception as e:
#             print(e)
#             pass
#
#
#     def parse_news(self, response):
#         # 抽取内容
#         EndText = response.css('#endText').extract()
#         content = extractLabelP(EndText)
#         # 抽取其他
#         title = response.css('h1::text').extract_first()
#         timee = response.css('.post_time_source::text').extract_first()
#         source = response.css('.post_time_source>a::text').extract_first()
#         creatTime = extractTime(timee)
#         newsItem = makeNewsItem(url=response.url,
#                                 docId=docId,
#                                 title=title,
#                                 createTime=creatTime,
#                                 content=content,
#                                 source=source)
#         # 生成
#         yield newsItem
#
#     def parse_dy(self,response):
#         EndText = response.css('#content').extract()
#         content = extractLabelP(EndText)
#         # 抽取其他
#         title = response.css('h2::text').extract_first().strip()
#         source = '网易号'
#         creatTime = response.css('.time>span::text').extract_first()
#         newsItem = makeNewsItem(url=response.url,
#                                 docId=response.meta,
#                                 title=title,
#                                 createTime=creatTime,
#                                 content=content,
#                                 source=source)
#         # 保存
#         yield newsItem
#
#     def parse_others(self,response):
#         # 尝试读取textArea
#         textAreaLabel = response.css('textarea::text').extract()
#         if textAreaLabel:
#             # 提取textArea内文本
#             nexturls, textAreaDic = extractTextArea(textAreaLabel)
#
#             # 保存读取的信息
#             textAreaDic['docId'] = docId
#             textAreaDic['url'] = response.url
#             newsItem = genaNewsItem(textAreaDic)
#             yield newsItem
#
#             # 读取下一个链接
#             for url in nexturls:
#                 yield response.urljoin(url=url, callback=self.parse_new)
#
#     """ 根据不同的类型提取新闻正文 """
#     def parse_new(self, response):
#         NewsUrl = response.url
#         # 新闻链接类型
#         whichType = howToExtractContent(NewsUrl)
#         # 准备所需信息
#         scrip_content = self.getScriptText(response)
#         docId = findKeyWordJson(html_content=scrip_content
#                                 , keyword='docId')
#
#         productKey = findKeyWordJson(html_content=scrip_content
#                                      , keyword='productKey')
#         # print(docId)
#         # print(productKey)
#         # 分析评论Api的第一页
#         # 需要在script中查找docId
#         # 提取 "docId"
#         new_url = concateCommentApi(productKey=productKey,
#                                     docId=docId,
#                                     offset='0',
#                                     ListType='newList')
#         print(new_url)
#         header = {'Host': 'comment.news.163.com',
#                   'Accept': '*/*',
#                   'Referer': response.url,
#                   'Accept-Encoding': 'gzip, deflate',
#                   'Accept-Language': 'zh-CN,zh;q=0.8'}
#         yield Request(url=new_url, callback=self.parse_comment)
#
#
#
#
#     def getScriptText(self,response):
#         scrip = response.css('script').extract()
#         scrip_content = "".join(scrip)
#         return scrip_content