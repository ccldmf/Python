from xml.sax.handler import ContentHandler
from xml.sax import parse

class HeadlineHandler(ContentHandler):		#所有标题元素

	in_headline = False

	def __init__(self,headlines):
		super().__init__()
		self.handlers = headlines
		self.data = []

	def startElement(self,name,attrs):	#定义元素开始处理事件函数
		if name == 'h1':
			self.in_headline = True

	def endElement(self,name):			#定义元素结束处理事件函数
		if name == 'h1':
			text = ''.join(self.data)
			self.data = []
			self.handlers.append(text)
			self.in_headline = False

	def characters(self,string):		#定义遇到字符处理事件函数
		if self.in_headline:
			self.data.append(string)	#将字符串添加至末尾

headlines = []
parse('website.xml',HeadlineHandler(headlines))

print('The following <h1> element were found:')
for h in headlines:
	print(h)