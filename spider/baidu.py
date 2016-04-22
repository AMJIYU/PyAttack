
#coding=utf-8
import urllib2
import urllib
import re
import time

'''
作用:根据用户输入规则:	inurl:gov.cn 爬取相应的网站。可以选择爬取的页数。
'''

class baidu:
	def __init__(self,queue,key_address):
		self.key_address=key_address         #关键字
		self.num=1000                              #抓取的条数
		self.x=1
		self.lists=[]
		self.queue=queue
		self.run()

	def run(self):
			self.search()

	def search(self):
		try:
			url = "http://www.baidu.com/s?wd=" + urllib.quote(self.key_address)+'&pn='+str(self.x)    #从百度抓取数据
			htmlbody=urllib2.urlopen(url).read()

			res=r'data-tools=\'\{\"title\":\".*\",\"url\":\"(.*)\"\}\'>'
			p_tel=re.compile(res)
			htmllist=p_tel.findall(htmlbody)

			for i in htmllist:
				try:
					f=urllib2.urlopen(i,timeout=5)
					url_true=f.geturl()

					print url_true

					self.lists.append(url_true)

					self.queue.put(url_true)       #将获取到的url存入队列中

					self.txt(url_true)

				except:
					pass
		except Exception,e:
			print e
			pass
		self.x+=1
		time.sleep(0.5)
		if self.x>self.num:
			pass
		else:
			self.search()

	def txt(self,i):                   #将爬取的url保存至txt备份
		f=open("logs/url.txt","a")
		f.write(i+"\n")
		f.close()