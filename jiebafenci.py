# -*- coding = utf-8 -*-
import csv存储
import jieba
import matplotlib
from collections import Counter
from pyecharts.charts import WordCloud
import wordcloud

def wordSegment():
    csvfile = open('知乎热榜.csv', mode='r') #读入csv文件
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
    wc.add(shape='diamond',series_name="知乎热榜" ,data_pair=wordCount.items(),word_size_range=[20,100])
    wc.render(r'知乎热榜高频词.html ')#输出到HTML文件

if __name__ == '__main__':
    wordlist = wordSegment()
    wordCloud(wordlist)