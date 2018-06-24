from xml.sax.handler import ContentHandler
from xml.sax import parse

class PageMaker(ContentHandler):		#所有标题元素

	passthrough = False

	def startElement(self,name,attrs):	#定义元素开始处理事件函数
		if name == 'page':
			self.passthrough = True
			self.out = open(attrs['name'] + '.html','w')
			self.out.write('<html><head>\n')
			self.out.write('<title>{}</title>\n'.format(attrs['title']))
			self.out.write('</head><body>\n')
		elif self.passthrough:
			self.out.write('<' + name)
			for key,val in attrs.items():
				self.out.write(' {}="{}"'.format(key,val))
			self.out.write('>')


	def endElement(self,name):			#定义元素结束处理事件函数
		if name == 'page':
			self.passthrough = False
			self.out.write('\n</body></html>\n')
			self.out.close()
		elif self.passthrough:
			self.out.write('</{}>'.format(name))

	def characters(self,chars):		#定义遇到字符处理事件函数
		if self.passthrough:
			self.out.write(chars)

parse('website.xml',PageMaker())