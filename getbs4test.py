# -*- coding = utf-8 -*-
import csv
import requests
from bs4 import BeautifulSoup  # 网页解析，获取数据
import re  # 正则表达式——进行文字匹配
import lxml
import urllib.request # 使用URL，获取网页数据
import urllib.error
import json


url = "https://www.zhihu.com/hot"

findlink = re.compile(r'<a data-za-not-track-link="true" href="(.*?)" rel=',re.S)  # 热榜链接
findid = re.compile(r'<div class="HotItem-rank HotItem-hot">(.*?)</div>',re.S)  # 热榜排名
findid2 = re.compile(r'<div class="HotItem-rank">(.*?)</div>',re.S)  # 热榜排名
findtitle = re.compile(r'<h2 class="HotItem-title">(.*?)</h2>',re.S)  # 热榜标题
findintroduce = re.compile(r'<p class="HotItem-excerpt">(.*?)</p>',re.S)  # 热榜内容
findscore = re.compile(r'</svg>(.*?)<span class="HotItem-action">',re.S)  # 热榜热度

def main():
    url = "https://www.zhihu.com/hot"
    # askURL(url)
    savehtml = htmlgetdata()
    print(savehtml)
    # write_to_file(savehtml)
    # saveData(savehtml)

def htmlgetdata():
    datalist = []
    html = open('知乎hot页面.html', 'r', encoding='utf-8')
    # print(html)
    # exit(1)
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all('section', class_="HotItem"):
        data = []
        item = str(item)
        # print(item)
        # exit(1)
        Id = re.findall(findid,item)
        # print(Id)
        # exit(1)
        if (len(Id) == 0):
            Id = re.findall(findid2,item)[0]
        else:
            Id = Id[0]
            # print(Id)
        # Id="热榜排名:"+Id.strip()
        Id =  Id.strip()
        data.append(Id)
        # print(Id)
        # exit(1)

        Link = re.findall(findlink, item)[0]
        # Link = "热榜链接:"+Link.strip()
        Link = Link.strip()
        data.append(Link)
        # print(Link)

        Title = re.findall(findtitle, item)[0]
        # Title = "热榜标题:"+Title.strip()
        Title = Title.strip()
        data.append(Title)
        # print(Title)

        Introduce = re.findall(findintroduce, item)
        if (len(Introduce) == 0):
            Introduce = "暂无"
        else:
            Introduce = Introduce[0]
        # Introduce = "热榜内容:"+Introduce.strip()
        Introduce = Introduce.strip()
        data.append(Introduce)
        # print(Introduce)

        Score = re.findall(findscore, item)[0]
        # Score = "热榜热度:"+Score.strip()
        Score = Score.strip()
        data.append(Score)
        # print(Score)
        datalist.append(data)
    # print(datalist)
    return datalist

def askURL(url):
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36',
            'cookies':'_zap=2e3aa90d-58dd-49ed-b982-51830f66e6bd; _xsrf=bfc7ef1a-9882-4829-b854-f4234aea597b; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1650706627; d_c0="AKBR17mF1RSPTl88-o6YCbw1h2m6rWzp8AI=|1650706627"; captcha_session_v2=2|1:0|10:1650706627|18:captcha_session_v2|88:OVY4WUxNOEhySlFwOFI1VTVaNEVPTnRCZnNBTzB3enZsaDczOGxSTEY1Z1ErM2ZPcVB3N1hOanBLRCsvM0dVaw==|c80fc750c38c88304d76425592935dc2f7f33a1e23ce5c1919ad4c2a153cdb2e; SESSIONID=kwyi8IiTKq9CX3aHJJMqALPlysCMiMyN9w9eVpiyLhm; JOID=UVoVBkJgG1w4RTWecWZwQE32tkBmCm4gXXd99SAha2d-EQz-O6DUNlxONpl4-MQz_gxKqoOwWQTO_68RphnTfc0=; osd=V10cBUtmHFU7TDOZeGV5Rkr_tUlgDWcjVHF6_CMobWB3EgX4PKnXP1pJP5px_sM6_QVMrYqzUALJ9qwYoB7afsQ=; __snaker__id=2JKRMa56kDc8WZSb; gdxidpyhxdE=aJCev8EwhVxB%2FEpL%2F9aLqmldNm%2BoT77LAN1p25SLmhEDId58gEUA8kzs%5CGngLaUKSJA4MdAHcCdPWd6h0VvUd6%2BmOdTr8hboSc3mPnb0Xad1ixiqE8Jb2x5Hl56WLyPHzQzV1xnewn273%2FS%2FXMMNZOfkYWznOD23Ib33DhSk0Qqa6kd%5C%3A1650707528091; _9755xjdesxxd_=32; YD00517437729195%3AWM_NI=PZAJvBbp3P9MowXTC2NXTqr2GU4TKXMH34VuNFAJ7Bcvi9FqueW6O%2F60ozrLfgweZttGQ5PTjkGYc4wL6m5mcmjV6kaI9p7%2BZmhtyJ2TK1HydrG%2Bvx%2BGmmO6JwM7P2YJS2s%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eebaf95f9691a1bbe55eade78eb7d15a878f8bb0c54e9593a394e74ba7f181d4e82af0fea7c3b92a94868fabf54aa2b0fdb1bc47ada998b5c23a8e889c92f13a858bfcb5ca548f98fdd5d57f8e9a8fabb64aa1aaa7dac57bb7bb99d7ce25f6f0a19bf148a6b9b986d980b8999fd6d360aab589bae240b594fa8eb867a1b3a6b7b561a397f791b6219ab3a895fc42f28c85d2cb73a8ae89ccf574e999a38ece3e8aa983d8d33a9b969dd3f237e2a3; YD00517437729195%3AWM_TID=C4PILbQPaiBEQRBBQAbVVHIitYELufmb; z_c0="2|1:0|10:1650707053|4:z_c0|92:Mi4xLXAxaElBQUFBQUFBb0ZIWHVZWFZGQ2NBQUFDRUFsVk5iVmVMWWdCVEl0VGJTWi13TlUwQVRBbVJaTFlJUnpUeXpR|fc882d88b2bef96c2b640d3c8b545a359f25724c57863acdba929e13742a4b27"; q_c1=8c04aec2fe134542b753d91e5532f3bc|1650707054000|1650707054000; tst=h; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1650707055; KLBRSID=81978cf28cf03c58e07f705c156aa833|1650707055|1650706626; NOT_UNREGISTER_WAITING=1'
            }
    response = requests.get(url=url,headers=head)
    # exit(1)
    try:
        html = response.text
        print(html)
        exit(1)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html

def saveData(datalist):
    with open('.\\知乎热榜.txt', 'w+', encoding='utf-8') as f:
        for i in datalist:
            f.write(json.dumps(i, ensure_ascii=False) + '\r\n')

def write_to_file(content):
    col = ["热榜排名", "热榜链接", "热榜标题", "热榜内容", "热榜热度"]
    with open('.\\知乎热榜.csv', 'w+',newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        for loop in range(50):
            if loop == 0:
               writer.writerow(col)
            else:
                writer.writerow(content[loop-1])

if __name__ == "__main__":
    main()
