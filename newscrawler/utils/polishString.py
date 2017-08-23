import re
import json
import random
from time import time
""" [ 会有重复 ]
    用于 rank 页面所有的链接读取
    给出一个区域，匹配所有的链接
"""
def reFindAllHref(selector_List):
    pattern = '<a[^>]+href="([^"]*)"[^>]*>([\s\S]*?)(?=</a>)'
    for i in selector_List:
        findList = re.findall(pattern=pattern, string=i.extract())
        for href, title in findList:
            yield href


""" 
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.78 Safari/537.36

'Host':'news.163.com',
'Host':'comment.news.163.com',
'Accept': '*/*',
'Referer': 'http://comment.news.163.com/news2_bbs/CSFEMKI30001899N.html',
'Accept-Encoding': 'gzip, deflate',
'Accept-Language': 'zh-CN,zh;q=0.8'

photo
Host: news.163.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8


"""


def getAttributeFromUrl(url,keyword):
    # http://comment.news.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/CSBMN1GN0001875P/comments/newList?offset=0&limit=30&showLevelThreshold=72&headLimit=1&tailLimit=2&callback=getData&ibc=newspc&_=1503375536399
    pattern = ''
    if keyword.lower() == 'productkey':
        pattern = 'products/(\w+)/threads'

    elif keyword.lower() == 'docid':
        pattern = 'threads/(\w+)/comments'
    else:
        # pattern = "[^\w]" + keyword + '=([^=&]+)'
        pattern = "[?&]" + keyword + '=([^=&]+)'
    res = re.search(pattern=pattern, string=url)
    if res:
        return res.group(1)
    return None

"""{
  "info": {
        "setname": "广州今年还有3条地铁开工 周边房价地图奉上",
        "lmodify": "2017-08-18 17:15:50",
        "prevue": "根据地铁官方公布，18、22、11号线将有望于年内全面开工，其中18、22号线涉及南沙与中心区的联系，11号线为广州首条“市区环线”。这个图集将为大家带来地铁房价地图以及简要的规划利好分析。（数据来源：中原研究发展部）",
        "source": "",
        "prev": {
            "seturl": "http://gz.house.163.com/photonew/0HKF0087/72783.html#q=1"
        },
        "next": {
            "seturl": "http://gz.house.163.com/photonew/0HKF0087/72782.html#q=1"
        }
 "list": [{
           "note": "18号线为南北走向，由南沙万顷沙-天河广州东站，其中经过天河、海珠、番禺、南沙4区。18号线与22号线定位同为南沙通往中心区的“快速通道”，目前沿线涉及琶洲互联网聚集区、横沥（明珠湾起步区）、万顷沙（枢纽区、保税港）等重点规划，由于横沥、万顷沙为南沙发展起步较晚，因此地铁线路未来有望引导人口流入，盘活片区发展活力。"
        },...]  note可能为空""
    }
"""
""" 尝试提取textArea内容 
    返回 文章文本，字典 
"""
def extractTextArea(textArea):
    if textArea:
        dicInfo = json.loads("".join(textArea))

        nexturls = [
            dicInfo['info']['prev']['seturl'],
            dicInfo['info']['next']['seturl'],
        ]
        title = dicInfo['info']['setname']
        abstract = dicInfo['info']['prevue']
        notes = [title,abstract]
        notelist = dicInfo['list']
        for i in notelist:
            if i['note']:
                notes.append(i['note'])
        news_content = "".join(notes)
        dicInfo['content']=news_content
        return nexturls,dicInfo




""" 抽取所有<p>标签内内容 """
def extractLabelP(html_content):
    pattern = '<p[^>]*>([^<>]*?)(?=</p>)'
    for txt in html_content:
        findall2 = re.findall(pattern=pattern, string=txt)
        return "".join(findall2)


def reFind(pattern ,string):
    return True if re.search(pattern=pattern ,string=string) else False

def strfind(string ,findstr):
    return string.find(findstr) != -1

typeNews = {
    'comment' :'comment',
    'news' :'news',
    'photoview' :'photoview',
    'dy' :'dy',
    'others' :'others'
}
def howToExtractContent(url):
    # http://news.163.com/17/0819/21/CS7USQM30001899N.html
    patternNews = r'http://\S+\.163\.com/\d{2}/\d{4}/\d+/\w+\.html'
    if strfind(findstr='comment.news.163.com/api/v1/products' ,string=url):
        return typeNews['comment']
    elif reFind(pattern=patternNews ,string=url):
        return typeNews['news']
    elif strfind(findstr='photoview' ,string=url):
        return typeNews['photoview']
    elif strfind(findstr='article/detail' ,string=url):
        return typeNews['dy'] # 网易号
    else:
        return typeNews['others'] # 尝试 访问textarea

# def test(response,start_urls):
#     for url in start_urls:
#         fetch(url)
#         content = ''
#         tabContents = response.css('.tabContents')
#         for x,y in reFindAllHref(tabContents):
#             t = howToExtractContent(x)
#             if t=='dy':
#                 pattern='\A(.+article/detail.+)\Z'
#                 print("dy:"+re.findall(pattern=pattern,string=x))
#             elif t=='photoview':
#                 pattern='\A(.+photoview.+)\Z'
#                 print("dy:"+re.findall(pattern=pattern,string=x))
#             else:
#                 pattern='\A(.+photonew.+)\Z'
#                 print("others:"+re.findall(pattern=pattern,string=x))




"""     
1.匹配.163.com/\d{2}/\d{4}/\d{2}/疑似16个\w.html
  (图集photoview另算)
2.寻找docId
3.寻找content或者endText，找不到则说明还有其他正文id，放弃即可
4.拼接得新commentApi，每次调取offset写新的
[直播] http://v.163.com/paike/VCHRH7PA5/VJR8LCOM5.html
    属于others，只需要评论没有正文
    docId是 docId:xx 的形式而不是 "docId" : "xxx"的json格式
    评论比较没营养
[专题 网易号]http://dy.163.com/v2/article/detail/CSBR18FG0515GFLV.html  
    id = 'content'
    普通方式在html中搜索docId，拼接CommentApi             
                [*]另一种sdk-api接口要求很严格：
                    http://sdk.comment.163.com/api/v1/products/a2869674571f77b5a0867c3d71db5856/threads/CSBR18FG0515GFLV/comments/newList?offset=0&limit=2&showLevelThreshold=70&headLimit=1&tailLimit=2&ibc=jssdk
                    &callback=tool1009860388490201624_1503377054054&_=1503377054055
[网易彩票]http://cai.163.com/article/17/0821/14/CSCATAAP00052DT2.html
    和普通新闻一样的
[房产图集]http://gz.house.163.com/photonew/5N620087/72861.html#p=CQP6K0JD5N620087NOS
    和普通图集一样
    不用正文直接评论即可
[槽值]http://caozhi.news.163.com/17/0821/12/CSC5PTA2000181TI.html
    id = 'endText' 
    普通方式在html中搜索docId，拼接CommentApi       
[图集]获得图集的唯一方式恐怕是爬取链接
    http://new(种类).163.com/photoview/00AO0001/2272018.html#p=CSECHHJ300AO0001NOS    
    ->  主要是 photoview
    -> (暂时不包括图集内容)
        name="gallery-data"  来自于 <textarea name="gallery-data" style="display:none;">
        textarea是唯一的，gallery-data也是唯一的
        匹配其后的json就可以获得数据
        {"info":{ 
            setname,lmodify,source
            有prev和next的图集链接，匹配xx.163.com/photoview/本图集数字加减可得链接
            }
         "list":[
            {匹配list中每一项的note是文字}             
         ]
        }
    ->  图集链接中的p不是真正的commentApi所需要的docId
        普通方式在html中搜索docId，拼接CommentApi           

"""



def stripToJSFormat(string):
    # left = string.find('(')
    # right = string.rfind(')')
    # return string[left:right+1]
    patternLeft = '([^\(]+\(|\);$)'
    res = re.sub(pattern=patternLeft ,string=string,
                 repl='')
    return res


""" 寻找 JSON 格式的 "keyword":"???" 
"""
def findKeyWordJson(html_content ,keyword):
    pattern = '"' + keyword + '"\s*:\s*"([^"]*?)"'
    re.search(string=html_content, pattern=pattern)
    search = re.search(pattern=pattern, string=html_content)
    if search:
        return search.group(1)
    return None


""" 根据内容 
生成新的 评论 js接口网址 
"""
def extractTime(string):
    pattern = '(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'
    res = re.search(string=string.strip(), pattern=pattern)
    if res:
        return res.group(1)


def concateCommentApi(productKey, docId, offset, ListType='newList'):
    limit = 30
    if ListType == 'newList':
        limit = 30
    elif ListType == 'hotList':
        limit = 40

    timestamp = str(int(time() * 1000))  # 13 char

    newListApi = \
        'http://comment.news.163.com/api/v1/products/' \
        + productKey + \
        '/threads/' \
        + docId + \
        '/comments/' \
        + ListType + \
        '?offset=' + offset + \
        '&limit=' + str(limit) + \
        '&showLevelThreshold=72&headLimit=1&tailLimit=2&callback=getData&ibc=newspc' \
        + str('&_=' + timestamp) if ListType == 'newList' else ''
        # + str('&_=' + timestamp)

    # 'a2869674571f77b5a0867c3d71db5856' \
    return newListApi
