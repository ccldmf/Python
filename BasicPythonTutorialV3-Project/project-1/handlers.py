#Handlers.py

class Handler:
	"""
	对Parser发起的方法调用进行处理的对象
	"""

	def callback(self,prefix,name,*args):			#回调函数  prefix:前缀  name:名称
		method = getattr(self,prefix + name,None)
		if callable(method):						#检查对象是否可调用
			return method(*args)

	def start(self,name):
		self.callback('start_',name)

	def end(self,name):
		self.callback('end_',name)

	def sub(self,name):
		def substitution(match):
			result =  self.callback('sub_',name,match)
			if result is None:
				match.group(0)
			return result
		return substitution


class HTMLRenderer(Handler):
	"""
	用于渲染HTML的具体处理程序
	"""

	def start_document(self):
		print('<html><head><title>...</title></head><body>')

	def end_document(self):
		print('</body></html>')

	def start_paragragh(slef):
		print('<p>')

	def end_paragragh(self):
		print('</p>')

	def start_heading(self):
		print('<h2>')

	def end_heading(self):
		print('</h2>')

	def start_list(self):
		print('<ul>')

	def end_list(self):
		print('</ul>')

	def start_listitem(self):
		print('<li>')

	def end_listitem(self):
		print('</li>')

	def start_title(self):
		print('<h1>')

	def end_title(self):
		print('</h1>')

	def sub_emphasis(self,match):
		return '<em>{}</em>'.format(match.group(1))

	def sub_url(self,match):
		return '<a href="{}">{}</a>'.format(match.group(1),match.group(1))

	def sub_mail(self,match):
		return '<a href="mailto:{}">{}</a>'.format(match.group(1),match.group(1))

	def feed(self,data):
		print(data)