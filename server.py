#-*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import json
import socket   #导入socket模块  
import re  
from multiprocessing import Process #导入进程模块  
  
#设置静态文件根目录  
HTML_ROOT_DIR='./html'  
def handle_client(client_socket):  
	"""处理客户端连接请求"""  
	request_data=client_socket.recv(1024)  
	print(request_data)  
	request_lines=request_data.splitlines()  
	for line in request_lines:  
		print(line)  
	#'GET / HTTP/1.1'  
	request_start_line=request_lines[0].decode("utf-8")  
	print("*"*10)  
	print(request_start_line)  
	response2=requests.get('http://kaijiang.500.com/static/info/kaijiang/xml/kl8/20180326.xml?_A=OCVBTSZE1522035057105')
	response2.encoding='gb18030'
	soup=BeautifulSoup(response2.text,'lxml');
	nums=soup.select('row',limit=6);
	arr={}
	i=0
	for num in nums:
		arr[i]={'expect':num['expect'],'opencode':num['opencode'],'opentime':num['opentime']};
		#print(key)
		i=i+1
	response_start_line="HTTP/1.1 200 ok\r\n"  
	response_heads="Server: My server\r\n"  
	response_body=arr 
	response=response_start_line+response_heads+"\r\n"+response_body  
	print("response data:",response)  
	client_socket.send(bytes(response,"utf-8"))  
	client_socket.close()  
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  # 创建socket对象  
	s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)  
	#host = socket.gethostname()  # 获取本地主机名  
	port = 1212  #  
	#print(host)  
	s.bind(("", port))  # 绑定端口  
	s.listen(5)  
	while True:  
		c,addr=s.accept()   #建立客户端连接  
		print('连接地址',addr)  
		handle_client_process=Process(target=handle_client,args=(c,))   #ALT+ENTER快捷键生成函数  
		handle_client_process.start()  
		c.close()  