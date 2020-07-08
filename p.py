def removeExtraNewline(filename, newfilename):
	f = open(filename, 'r')
	newfile = open(newfilename, 'w')
	lines = f.readlines()

	for i in range(len(lines)):
		if(i == 0):
			continue
		if(i+1 <= len(lines)-1 and lines[i] == "\n" and lines[i+1] == "\n"):
			continue
		newfile.write(lines[i])
	f.close()
	newfile.close()

def removeFirstLastNewline(filename, newfilename):
	f = open(filename, 'r')
	newfile = open(newfilename, 'w')
	lines = f.readlines()

	for i in range(len(lines)):
		if(i == 0 and lines[i] == "\n"):
			continue
		if(i == len(lines)-1 and lines[i] == "\n"):
			continue
		newfile.write(lines[i])
	f.close()
	newfile.close()

def removeLastTwoLines(filename, newfilename):
	f = open(filename, 'r')
	newfile = open(newfilename, 'w')
	lines = f.readlines()

	for i in range(len(lines)):
		if(i == len(lines)-1 or i == len(lines)-2):
			continue
		newfile.write(lines[i])
	f.close()
	newfile.close()

startnum = 1
endnum = 7
letter = "d"

for i in range(startnum, endnum+1):
	filename = letter + '0'*(4-len(str(i))) + str(i) + '.txt'
	newfilename = "yy.txt"
	removeExtraNewline(filename, newfilename)

	filename = "yy.txt"
	newfilename = "zz.txt"
	removeFirstLastNewline(filename, newfilename)

	filename = "zz.txt"
	newfilename = 's' + letter + '0'*(4-len(str(i))) + str(i) + '.txt'
	removeLastTwoLines(filename, newfilename)