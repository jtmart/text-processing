from random import randint as ra
Titles = []
Months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August',
		  'September', 'October', 'November', 'December']
names = []

def correctSpacingInLines(l):
	length = len(l)
	i = 1
	while(i < length-1):
		if(ord(l[i]) == 10):
			if(l[i-2] != '.' and l[i-1] != '\n'):
				l = l[:i] + l[i+1:]
				length -= 1
				i -= 1
		i+=1
	return l

def findYear(year):
	j = 0
	length = len(year)
	while(j < length):
		if year[j] == ' ':
			year = year[:j] + year[j+1:]
			length -= 1
		j+=1
	return year[:4]

def findMonth(st):
	if(st[-1] == ' '):
		st = st[:-1]

	mon = st.split(" ")
	mon = mon[-2]
	indi = 0
	for i in range(12):
		if Months[i] == mon:
			indi = i+1
			break
	month = str(indi)
	if(len(month) == 1):
		month = '0' + month
	return month

def findDate(st):
	if(st[-1] == ' '):
		st = st[:-1]

	dat = st.split(" ")
	date = dat[-1]
	if(len(date) == 1):
		date = '0' + date
	return date

def fileName():
	global names

	file = open("Footer.txt")
	data = file.read().split('\n')[:-1]
	file.close()

	randomCollection = []
	count = 1
	for i in data:
		string = i.split(",")
		year = findYear(string[-1])
		month = findMonth(string[-2])
		date = findDate(string[-2])
		# print(count," | ",date, month, year)
		count += 1
		random = ra(100001,999999)
		while(random in randomCollection):
			random = ra(100001,999999)
		names.append('t' + year + month + date + str(random))

fileName()
# for c in names:
# 	print(c)

for i in range(1,len(names)+1):
	file = open("temp/speech" + str(i) + ".txt")
	l = file.read()
	file.close()

# 	# l = correctSpacingInLines(l)

	file = open("ori/" + names[i-1] + ".txt","w+")
	file.write(l)
	file.close()

file = open("Titles.txt")
Titles = file.read().split('\n')[:-1]
file.close()

titles = ""
for i in range(len(names)):
	titles += Titles[i] + "|" + names[i] + '\n'

file = open("Titles2.txt","w+")
file.write(titles)
file.close()
