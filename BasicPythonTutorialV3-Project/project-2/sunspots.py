#sunspots.py
from urllib.request import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = 'ftp://ftp.swpc.noaa.gov/pub/weekly/Predict.txt'   #获取数据
COMMENT_CHARS = '#:'		#共有字符

drawing = Drawing(400,200)	#Drawing对象
data = []					#数据列表
for line in urlopen(URL).readlines():	#从数据源中读取数据
	line = line.decode()				#将读到的数据以字符串格式进行编码
	if not line.isspace() and line[0] not in COMMENT_CHARS:		#判断字符串是否为空且开头不能是包含#：(注释)
		data.append([float(n) for n in line.split()])	#将每行的字符串进行切片，并将获得数据转换为float型

pred = [row[2] for row in data]			#获得每行数据中的第3个数据，即pred，并将所有值存放在列表中
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [list(zip(times,pred)),			#将时间和pred值合并成元组列表
		   list(zip(times,high)),
		   list(zip(times,low))]

lp.lines[0].strokeColor = colors.blue		#设置颜色
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

drawing.add(lp)			#添加折线

drawing.add(String(250,150,'Sunspots',fontSize=14,fillColor=colors.red))
renderPDF.drawToFile(drawing,'report2.pdf','Sunspots')		#保存文件

