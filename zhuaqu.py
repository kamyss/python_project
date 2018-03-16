#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
response=requests.get('http://kaijiang.500.com/?0_ala_baidu');
#print(response.text)
soup=BeautifulSoup(response.text,'lxml');
#nums=soup.find_all(class_='td_kjhm01',limit=6);
nums=soup.select('.td_kjhm01',limit=6);
for num in nums:
	print(num.get_text())