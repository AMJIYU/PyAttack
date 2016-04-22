#!coding=utf-8

from google import search

class s_google:
	def __init__(self,queue,keyword):
		self.queue=queue
		self.keyword=keyword
		self.run()

	def run(self):
		print self.keyword
		for url in search(self.keyword):
			print url
			self.queue.put(url)

		