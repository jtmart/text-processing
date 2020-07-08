import os

def correct100():
	for f in os.listdir('.'):
		if (not f.endswith('py') and len(f) == 2):
			os.rename(f, '1'+f)  

def correctnumbering(currrent, actual):
	dif = actual - currrent
	for f in os.listdir('.'):
		if (not f.endswith('py')):
			num = f[:len(f) - 4]
			newname = str(int(num) + dif)
			os.rename(f, newname)  

def numtotxt():
	for f in os.listdir('.'):
		if (not f.endswith('py') and not f.endswith('txt')):
			os.rename(f, f+'.txt')  


def prepend(starting):
	for f in os.listdir('.'):
		if (not f.startswith(starting) and f.endswith('txt')):
			name = f[:len(f) - 4]
			zero = 4 - len(name)
			newname = starting + '0'*zero + f
			os.rename(f, newname)


correctnumbering(1, 216)
numtotxt()
prepend('e')