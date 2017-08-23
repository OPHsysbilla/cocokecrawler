SAVE_COMMENT_DIR = r'D:\MongoDB\savejson\comment'
SAVE_NEWS_DIR = SAVE_COMMENT_DIR




# tag = getattr(self, 'tag', None)
#     url = url + 'tag/' + tag

# def findTophref(self,response):
#     tabContents = response.css('.tabContents')
#     reFindAllHref(tabContents)
#
#     EndText = response.css('#endText').extract()
#     extractLabelP(EndText)
#
#     # 找docId
#
#
# def ShowAll(self,response,startUrls):
#     for url in startUrls:
#         fetch(url)
#
#         tabContents = response.css('.tabContents')
#         for x,y in reFindAllHref(tabContents):
#             whichType = howToExtractContent(x)
#             fetch(x)
#
#             NewsUrl = response.url
#             scrip_content = self.getScriptText(response)
#             docId = findKeyWordJson(html_content=scrip_content
#                                     , keyword='docId')
#             productKey = findKeyWordJson(html_content=scrip_content
#                                          , keyword='productKey')
#
#             if whichType == typeNews['news']:
#                 # 抽取内容
#                 EndText = response.css('#endText').extract()
#                 content = extractLabelP(EndText)
#                 # 抽取其他
#
#                 title = response.css('h1::text').extract_first()
#                 timee = response.css('.post_time_source::text').extract_first()
#                 source =  response.css('.post_time_source>a::text').extract_first()
#                 creatTime = extractTime(timee)
#                 dicN = makeNewsDict(url=NewsUrl,
#                                     docId=docId,
#                                     title=title,
#                                     createTime=creatTime,
#                                     content=content,
#                                     source=source)
#                 # 保存
#                 saveNews(dicN)
#
#             # 网易号 ,id = content
#             elif whichType== typeNews['dy']:
#                 EndText = response.css('#content').extract()
#                 content = extractLabelP(EndText)
#                 # 抽取其他
#                 title = response.css('h2::text').extract_first().strip()
#                 source = '网易号'
#                 creatTime = response.css('.time>span::text').extract_first()
#                 dicN = makeNewsDict(url=NewsUrl,
#                                     docId=docId,
#                                     title=title,
#                                     createTime=creatTime,
#                                     content=content,
#                                     source=source)
#                 # 保存
#                 saveNews(dicN)
#
#             # 图集，是读取textArea内的内容
#             # others可以不管正文，一般是直播之类的
#             elif whichType== typeNews['photoview'] or whichType==typeNews['others'] :
#                 # 尝试读取textArea
#                 textAreaLabel = response.css('textarea::text').extract()
#                 if textAreaLabel:
#                     # 提取textArea内文本
#                     nexturls,textAreaDic = extractTextArea(textAreaLabel)
#                     # 读取下一个链接
#                     for url in nexturls:
#                         yield Request(url=url, callback=self.parse_new)
#                     # 保存读取的信息
#                     textAreaDic['docId']=docId
#                     textAreaDic['url']=NewsUrl
#                     saveNews(textAreaDic)
#
#             # 分析评论Api的第一页
#             # 需要在script中查找docId
#             # 提取 "docId"
#
#             new_url = generateCommentApi(scrip_content=scrip_content,
#                                          offset=0,
#                                          docId=docId,
#                                          productKey=productKey,
#                                          ListType='newList')
#             yield Request(url=new_url, callback=self.parse_comment)
