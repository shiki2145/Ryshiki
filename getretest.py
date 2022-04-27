# -*- coding = utf-8 -*-
import requests
import re  # 正则表达式——进行文字匹配
import lxml
import json


pattern = re.compile(
                     '<div class="HotItem-index">.*?>(.*?)</div>.*?'
                     '<a data-za-not-track-link="true" href="(.*?)" rel=.*?'
                     '<h2 class="HotItem-title">(.*?)</h2>.*?'
                     '(.*?)</a>.*?'
                     '</svg>(.*?)<span class="HotItem-action">'
                     ,re.S)
def main():
    url = "https://www.zhihu.com/hot"
    # askURL(url)
    htmlgetdata()
    # saveData(savehtml)

def htmlgetdata():
    datalist = []
    html = open('知乎hot页面.html', 'r',encoding= ' utf-8 ' )
    html=html.read()
    items = re.findall(pattern,html)
    for item in items:
        id ="热榜排名:" + item[0].strip()
        link ="热榜链接:" + item[1].strip()
        title ="热榜标题:" + item[2].strip()
        intro = "热榜内容:" + item[3].replace('<p class="HotItem-excerpt">','').replace('</p>','').strip()
        num = "热榜热度:" + item[4].strip()
        data=(id,link,title,intro,num)
        datalist.append(data)
    print(len(datalist))
    # exit(1)
    print(datalist)
    # exit(1)

if __name__ == "__main__":
    main()