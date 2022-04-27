# -*- coding = utf-8 -*-
from lxml import etree
import urllib.request, urllib.error

import json

def getData(baseurl):
     datalist=[]
     htmltxt = askURL(baseurl)
     # print(html)
     # exit(1)
     html = etree.HTML(htmltxt)
     Rank = html.xpath('//a/div/div[@class="css-blkmyu"or@class="css-mm8qdi"]/text()')
     Link = html.xpath('//a[@class="css-hi1lih"]/@href')
     Title = html.xpath('//a[@class="css-hi1lih"]/div/h1[@class="css-3yucnr"]/text()')
     Introducelist =[]
     for i in range(1,51):
          a = ('//a[%s][@class="css-hi1lih"]/div/div[@class="css-1o6sw4j"]/text()'%i)
          Introduce = html.xpath(a)
          if (len(Introduce) == 0):
               Introduce = ["暂无"]
          Introducelist.append(Introduce[0])
     Score = html.xpath('//a[@class="css-hi1lih"]/div/div[@class="css-1iqwfle"]/text()')
     # print(Score)
     # print(len(Score))
     # exit(1)
     # print(len(Rank))
     # print(len(Link))
     # print(len(Title))
     # print(len(Introducelist))
     # print(len(Score))
     for i in range(0,50):
          data = []
          id=("热榜排名:" + Rank[i].strip())
          link =("热榜链接:" + Link[i].strip())
          title =("热榜标题:" + Title[i].strip())
          intro =("热榜内容:" + Introducelist[i].strip())
          score = ("热榜热度:" + Score[i].strip())
          data.append(id)
          data.append(link)
          data.append(title)
          data.append(intro)
          data.append(score)
          datalist.append(data)
     return datalist

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
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html

def saveData(datalist):
    with open('.\\xpath知乎热榜.txt', 'w+', encoding='utf-8') as f:
        for i in datalist:
            f.write(json.dumps(i, ensure_ascii=False) + '\r\n')

if __name__ == "__main__":
        url = "https://www.zhihu.com/hot"
        # htmlgetdata(url)
        datalist = getData(url)
        saveData(datalist)