#util.py

def lines(file):
	for line in file:yield line
	yield '\n'

def blocks(file):
	block = []
	for line in lines(file):
		if line.strip():		#去字符串首尾空格
			block.append(line)	#将字符串加到列表中
		elif block:
			yield ''.join(block).strip()
			block = []