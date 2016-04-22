#!coding=utf-8
import httplib
import time

class webdav:
	def __init__(self,urls):
		self.headers = {
		           'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:37.0) Gecko/20100101 Firefox/37.0'
		        }
		self.urls=urls
		self.tag=[u"防火墙",u"安全狗",u"访问禁止",u"操作失败"]
		self.b=0
		
	def run(self):
		if self.jar("PUT"):
			if self.jar("COPY") or self.jar("MOVE"):
				r='%s :has webdav' % self.urls
				c=time.ctime()
				f=open("output/output.txt","a")
				f.write(r+"\n"+" "+c)
				f.close()
				print "[*webdav*]"+self.urls
			else:
				#print '%s :not has webdav' % self.urls
				pass
		else:
			#print '%s :not has webdav' % self.urls
			pass


	def bodys(self):        #源码需要解码成unicode格式
		try:
			self.body.decode("utf-8")         
		except:
			try:
				self.body.decode("gbk")
			except:
				try:
					self.body.decode("gb2312")
				except:
					self.tag=["防火墙","安全狗","访问禁止","操作失败"]


	def jar(self,option):            #webdav判断函数
		try:
			#print 'dav',self.urls
			conn=httplib.HTTPConnection(self.urls,80,True,5)
			conn.request(option+" /a.txt",'/','',headers=self.headers)
			res=conn.getresponse()
			self.body=str(res.read())
			header=str(res.msg)
			status=str(res.status)
			try:
				lengths=int(res.length)
			except:
				lengths=0
			self.bodys()                    #处理源码
			
			if status=="200":               #首先判断返回码
				if lengths!=915:            #再判断返回主体内容长度
					if "WAF" not in header: #如果头中存在WAF关键字，则不成功
						for i in self.tag:  #源码中匹配关键字，如存在这些关键字，则说明不成功
							if i in self.body:  
								self.b=1

							if self.b==1:
								return False
							else:
								return True
					else:
						return False
				else:
					return False
			else:
				return False
			conn.close()

		except Exception,e:
			#print "webdav",e
			return False


