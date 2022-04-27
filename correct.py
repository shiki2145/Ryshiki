# -*- coding = utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

soup = BeautifulSoup(open('知乎hot页面.html',encoding="utf-8"),'lxml')
file1 = open('知乎hot页面.html', 'w+',encoding= ' utf-8 ' )
# soup = BeautifulSoup(open('newhot.html',encoding="utf-8"),'lxml')
# file1 = open('newhot.html', 'w',encoding= ' utf-8 ' )
file1.write(soup.prettify())
file1.close()
