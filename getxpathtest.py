# -*- coding = utf-8 -*-
from lxml import etree


html = etree.parse('./知乎hot页面.html',etree.HTMLParser())#
Rank = html.xpath('//div[@class="HotItem-index"]/div[@class="HotItem-rank"or@class="HotItem-rank HotItem-hot"]/text()')
Link = html.xpath('//div[@class="HotItem-content"]/a/@href')
Title = html.xpath('//div[@class="HotItem-content"]/a/h2[@class="HotItem-title"]/text()')
Introducelist =[]
for i in range(1,51):
     a = ('//section[%s]/div[@class="HotItem-content"]/a/p/text()'%i)
     Introduce = html.xpath(a)
     if (len(Introduce) == 0):
          Introduce = ["暂无"]
     Introducelist.append(Introduce[0])
Score = html.xpath('//div[@class="HotItem-content"]/div/text()[3]')

# print(len(Rank))
# print(len(Link))
# print(len(Title))
# print(len(Introducelist))
# print(len(Score))

for i in range(0,50):
     print("热榜排名:" + Rank[i].strip())
     print("热榜链接:" + Link[i].strip())
     print("热榜标题:" + Title[i].strip())
     print("热榜内容:" + Introducelist[i].strip())
     print("热榜热度:" + Score[i].strip())