#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import sys 
reload(sys)   
sys.setdefaultencoding('utf8')
response=requests.get('https://juejin.im/timeline');
#response.encoding='gb18030'
#print(response.text)
soup=BeautifulSoup(response.text,'lxml');
#print(soup);
#nums=soup.find_all(id="ssl_expect_detail",limit=6);
#nums=soup.find_all(class_='td_kjhm01',limit=6);
#nums=soup.select('tbody tr td',limit=6);
#让标签格式对齐
#soup=soup.prettify()
#如果要定位到具体的点，我们可以靠浏览器的copy-selector进行快速定位
titles=soup.select('#juejin > div.view-container > main > div > div > ul');
print(titles)
for title in titles:
	print(title.string)
