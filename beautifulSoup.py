#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse">< b>The Dormouse's story</b>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister haha" id="link1">< !-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story">...</p>
</body>
</html>
"""

#html='<html><head></head><body><div><img src="http://666.png" /></div></body></html>';
soup=BeautifulSoup(html,'lxml');
# -*- coding:utf8 -*-
#获取某个标签节点内容的方法;
print (soup.head);
#输出标签名
print(soup.head.name)
#输出属性对象
print(soup.a.attrs)
#输出属性对象的具体值
print(soup.a.attrs['href'])
#输出标签属性的class,注意：class有多个取出来是一个数组
print(soup.a.attrs['class'][0]);
#获取的第一种简写形式
print(soup.a['href'])
#第二种简写形式
print(soup.a.get('href'));
#string可以取得标签的完整内容
print(soup.a.string);
#get_text可以获取标签中的所有内容
print(soup.html.get_text());
#获取所有的标签进行遍历
ps=soup.find_all('a');
for p in ps:
	print(p.get('href'))#得到a标签的属性
#传入正则表达式：soup.find_all(re.compile(r'^b')查找以b开头的所有标签，这里的body和b标签都会被查到
#要装re库
#soup.find_all(re.compile(r'^b'))
#同时找到两个标签
soup.find_all(["a","b"])
#通过keywords来进行页面的内容的提取
#查找id值为link2的标签对象
idLink=soup.find_all(id='link2');
print(idLink[0].get('href'))
#以类为条件获取找class要加下划线为class_因为是关键词
diLink2=soup.find_all(class_='sister');
print(diLink2[2].get('href'))
#同时满足的条件
diLink3=soup.find_all(class_='sister',id='link3');
print(diLink3[0]['href']);
#通过标签内容来查找标签对象
textInfo=soup.find_all(text="Lacie")
print(textInfo);
#为了加快速度可以限制数量
limitS=soup.find_all('a',limit=2);
print('--------------------------------------')
for lm in limitS:
	print(lm.get('href'))
#一维的查询用find();
print(soup.find('a').get('href'))
#select函数可以像传统的选择器写法那样调用
print('-----------------------------');
selectList=soup.select('.sister');
for ls in selectList:
	print(ls.get('href'))
#组合查找
print soup.select('p #link1')    #查找p标签中内容为id属性为link1的标签
#[]
print soup.select("head > title")   #直接查找子标签
#[]
#属性查询
print soup.select('a[class="sister"]')
#[< a class="sister" href="http://example.com/elsie" id="link1">< !-- Elsie -->< /a>, < a class="sister" href="http://example.com/lacie" id="link2">Lacie< /a>, < a class="sister" href="http://example.com/tillie" id="link3">Tillie< /a>]
print soup.select('a[href="http://example.com/elsie"]')
#[< a class="sister" href="http://example.com/elsie" id="link1">< !-- Elsie -->< /a>]
print soup.select('p a[href="http://example.com/elsie"]')
#[< a class="sister" href="http://example.com/elsie" id="link1">< !-- Elsie -->< /a>]