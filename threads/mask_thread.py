#!coding=utf-8
'''
多线程
'''

import threading
import urlparse
from script.WebDav import webdav
from script.Ewebeditor import ewebeditor
from script.Struts2 import struts2
from script.Struts2_032 import struts2_032

maxs=10
th=threading.BoundedSemaphore(maxs)
class mask_thread(threading.Thread):
	def __init__(self,t_name,queue,list_paths,names):
		threading.Thread.__init__(self,name=t_name)
		self.queue=queue
		self.list_paths=list_paths
		self.name=names
		
	def run(self):
		th.acquire()
		try:
			self.urls=self.queue.get().replace("\n","").strip()  #如果队列为空，不阻塞
		except:
			pass
		else:
			self.get()  
			try:
				name_list=self.name.split(",")
				for i in name_list:
					if i=="ewebeditor" or i=="1":
						ewebeditor(self.domain,self.list_paths).run()       #漏洞检测主体
					elif i=="webdav" or i=="2":
						webdav(self.domain).run()
					elif i=="struts2" or i=="3":
						struts2(self.urls)
						struts2_032(self.urls)
					elif i=="all":
						ewebeditor(self.domain,self.list_paths).run()
						webdav(self.domain).run()
						struts2(self.urls)
					else:
						break

			except Exception,e:
				print e
				pass
			th.release()

	def get(self):                     #从队列中取出数据(url)            
		try:
			self.domain=urlparse.urlparse(self.urls).netloc
		except:
			self.domain=""