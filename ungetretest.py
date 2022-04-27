# -*- coding = utf-8 -*-
import csv
import jieba
from collections import Counter
from pyecharts.charts import WordCloud

import requests
import re  # 正则表达式——进行文字匹配
import lxml
import urllib.request # 使用URL，获取网页数据
import urllib.error
import json
import csv存储

a='<style data-emotion-css="prh7s4">.css-prh7s4{display:-webkit-box;text-overflow:ellipsis;overflow:hidden;-webkit-box-orient:vertical;-webkit-line-clamp:1;}</style><style data-emotion-css="1o6sw4j">.css-1o6sw4j{box-sizing:border-box;margin:0;min-width:0;margin-top:4px;color:#444444;font-size:14px;display:-webkit-box;text-overflow:ellipsis;overflow:hidden;-webkit-box-orient:vertical;-webkit-line-clamp:1;}</style>'
b='<style data-emotion-css="1iqwfle">.css-1iqwfle{box-sizing:border-box;margin:0;min-width:0;color:#8590A6;font-weight:500;font-size:12px;margin-top:8px;}</style>'
pattern = re.compile(
                     '<a href="(.*?)".*?'
                     '<div class="css-(blkmyu|mm8qdi)">(.*?)</div>.*?'
                     '<h1 class="css-3yucnr">(.*?)</h1>.*?'
                     '(.*?)<div class="css-1iqwfle">.*?'
                     '(.*?)</div>'
                     ,re.S)
findlink = re.compile(r'<a href="(.*?)"',re.S)

def htmlgetdata(baseurl):
    datalist = []
    # html = open('newhot.html', 'r',encoding= ' utf-8 ' )
    # html=html.read()
    html = askURL(baseurl)
    # print(html)
    items = re.findall(pattern ,html)
    # print(items)
    # print(len(items))
    # exit(1)
    for item in items:
        if len(item[1])>3:
            id ="热榜排名:" + item[2]
        else:
            id = "热榜排名:" + item[1]
        link ="热榜链接:" + item[0]
        title ="热榜标题:" + item[3]
        intro = "热榜内容:" + item[4].replace('<div class="css-1o6sw4j">','').replace('</div>','').replace(a,'').replace(b,'')
        num = "热榜热度:" + item[5]
        data=(id.strip(),link.strip(),title.strip(),intro.strip(),num.strip())
        datalist.append(data)
    return datalist
    # print(len(datalist))
    # exit(1)
    # print(datalist)
    # exit(1)

def askURL(baseurl):
    # 设置请求头
    head = {
        "User-Agent": "Mozilla / 5.0(iPhone;CPUiPhoneOS13_2_3likeMacOSX) AppleWebKit / 605.1.15(KHTML, likeGecko) Version / 13.0.3Mobile / 15E148Safari / 604.1"
        ,'cookies':'_zap=2e3aa90d-58dd-49ed-b982-51830f66e6bd; d_c0="AKBR17mF1RSPTl88-o6YCbw1h2m6rWzp8AI=|1650706627"; captcha_session_v2=2|1:0|10:1650706627|18:captcha_session_v2|88:OVY4WUxNOEhySlFwOFI1VTVaNEVPTnRCZnNBTzB3enZsaDczOGxSTEY1Z1ErM2ZPcVB3N1hOanBLRCsvM0dVaw==|c80fc750c38c88304d76425592935dc2f7f33a1e23ce5c1919ad4c2a153cdb2e; __snaker__id=2JKRMa56kDc8WZSb; gdxidpyhxdE=aJCev8EwhVxB%2FEpL%2F9aLqmldNm%2BoT77LAN1p25SLmhEDId58gEUA8kzs%5CGngLaUKSJA4MdAHcCdPWd6h0VvUd6%2BmOdTr8hboSc3mPnb0Xad1ixiqE8Jb2x5Hl56WLyPHzQzV1xnewn273%2FS%2FXMMNZOfkYWznOD23Ib33DhSk0Qqa6kd%5C%3A1650707528091; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=PZAJvBbp3P9MowXTC2NXTqr2GU4TKXMH34VuNFAJ7Bcvi9FqueW6O%2F60ozrLfgweZttGQ5PTjkGYc4wL6m5mcmjV6kaI9p7%2BZmhtyJ2TK1HydrG%2Bvx%2BGmmO6JwM7P2YJS2s%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eebaf95f9691a1bbe55eade78eb7d15a878f8bb0c54e9593a394e74ba7f181d4e82af0fea7c3b92a94868fabf54aa2b0fdb1bc47ada998b5c23a8e889c92f13a858bfcb5ca548f98fdd5d57f8e9a8fabb64aa1aaa7dac57bb7bb99d7ce25f6f0a19bf148a6b9b986d980b8999fd6d360aab589bae240b594fa8eb867a1b3a6b7b561a397f791b6219ab3a895fc42f28c85d2cb73a8ae89ccf574e999a38ece3e8aa983d8d33a9b969dd3f237e2a3; YD00517437729195%3AWM_TID=C4PILbQPaiBEQRBBQAbVVHIitYELufmb; z_c0="2|1:0|10:1650707053|4:z_c0|92:Mi4xLXAxaElBQUFBQUFBb0ZIWHVZWFZGQ2NBQUFDRUFsVk5iVmVMWWdCVEl0VGJTWi13TlUwQVRBbVJaTFlJUnpUeXpR|fc882d88b2bef96c2b640d3c8b545a359f25724c57863acdba929e13742a4b27"; q_c1=8c04aec2fe134542b753d91e5532f3bc|1650707054000|1650707054000; _xsrf=Hx2fBz1pexSYp7omEBS7SUDv036Ukutu; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1650706627,1650960462; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1650960462; tst=h; NOT_UNREGISTER_WAITING=1; SESSIONID=TbgRm1keSPKPIBxzTUTqGyqgUF7TG9mOJWG6COK4L1f; JOID=VV0SB05lfCygWNRzXmYcM9PgUqZKMxxI8zfnGjg0LmXzEJQJJjXVScFY1HJcTh0OYUdhX208kx8A5Dx9EQbfuXQ=; osd=UFoRAU1gey-mW9F0XWAfNtTjVKVPNB9O8DLgGT43K2LwFpcMITbTSsRf13RfSxoNZ0RkWG46kBoH5zp-FAHcv3c=; KLBRSID=dc02df4a8178e8c4dfd0a3c8cbd8c726|1650960467|1650960462'

    }
    request = urllib.request.Request(baseurl, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
        # exit(1)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def saveData(datalist):
    with open('.\\re知乎热榜.txt', 'w+', encoding='utf-8') as f:
        for i in datalist:
            f.write(json.dumps(i, ensure_ascii=False) + '\r\n')

def write_to_file(content):
    col = ["热榜排名", "热榜链接", "热榜标题", "热榜内容", "热榜热度"]
    with open('.\\re知乎热榜.csv', 'w+',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        for loop in range(51):
            if loop == 0:
               writer.writerow(col)
            else:
                writer.writerow(content[loop-1])

def wordSegment():
    csvfile = open('re知乎热榜.csv', mode='r',encoding='UTF-8') #读入csv文件
    reader = csv.reader(csvfile)
    text =''
    for row in reader:
        text = text + ' ' + row[2] + ' ' + row[3]
    csvfile.close()
    # 使用jieba分词进行文本切割
    wordlist = jieba.lcut(text)#删除停用词
    stopwords = [line.strip() for line in open('.\\cn_stopwords.txt',encoding='UTF-8').readlines()]#这里加载停用词的路径
    wordlist =[x for x in wordlist if len(x) > 1 and x not in stopwords] #删除停用词以及词频小于2的词
    return wordlist

def wordCloud(wordlist):
    wordCount = Counter(wordlist)#词频统计
    # print(wordCount)
    wc = WordCloud()
    #seies.name:系列条称,用于tooltip的显示legend的图例筛选
    #word_size_range:单词字体大小范围，
    # data_pair:系列数据项，[(word1,count1),(word2,count2)]
    wc.add(shape='diamond',series_name="re知乎热榜" ,data_pair=wordCount.items(),word_size_range=[20,100])
    wc.render(r're知乎热榜高频词.html ')#输出到HTML文件


if __name__ == "__main__":
        url = "https://www.zhihu.com/hot"
        # htmlgetdata(url)
        datalist = htmlgetdata(url)
        # saveData(datalist)
        write_to_file(datalist)
        wordlist = wordSegment()
        wordCloud(wordlist)