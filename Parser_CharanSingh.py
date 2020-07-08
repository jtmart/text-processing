import random
import csv
# Must correct heading in Mother Teresa Speech, include in one line
# Correct heading of HEALTH: A TOP PRIORITY in index

speech_file= open("CharanSingh_Speeches.txt", "r")
data = speech_file.readlines()
index = dict()
speech_file.close()

def remove_fileHeaders():
	global data
	for i in range(len(data)):
		if data[i].rstrip()=="Contents":
			data=data[i:]
			break
def extract_contents():
	global data
	ctr=1
	for i in range(len(data)):
		if data[i].isupper():
			date=extract_date(data, i+1)
			index[data[i][:-2]]= date
			ctr+=1
		if "MESSAGES AND TRIBUTES" in index:
			index.pop("MESSAGES AND TRIBUTES")
			ctr-=1
		if "THE HOCKEY WIZARD" in index:
			data=data[i+19:]
			break

def extract_date(data, i):
	j=i
	while True:
		try:
			int(data[j][-3])
			line = data[j]
			month,find, end=get_month(line)
			day = line[find-3:find-1]
			year = line[find+end+1:find+end+5]
			return year+month+day
			break
		except:
			j+=1

def get_month(line):
	if "January" in line:
		f=line.find("January")
		return ("01",f, 7)
	elif "February" in line:
		f=line.find("February")
		return ("02",f,8)
	elif "March" in line:
		f=line.find("March")
		return ("03",f,5)
	elif "April" in line:
		f=line.find("April")
		return ("04",f,5)
	elif "May" in line:
		f=line.find("May")
		return ("05",f,3)
	elif "June" in line:
		f=line.find("June")
		return ("06",f,4)
	elif "July" in line:
		f=line.find("July")
		return ("07",f,4)
	elif "August" in line:
		f=line.find("August")
		return ("08",f,6)
	elif "September" in line:
		f=line.find("September")
		return ("09",f,9)
	elif "October" in line:
		f=line.find("October")
		return ("10",f,7)
	elif "November" in line:
		f=line.find("November")
		return ("11",f,8)
	elif "December" in line:
		f=line.find("December")
		return ("12",f,8)
	else:
		return -1

remove_fileHeaders()
extract_contents()
i=0
ctr=0
list=[]
while i < len(data):
	if data[i].upper()[:-2] in index:
		j=i+3
		flg=True
		list.append(index[data[i].upper()[:-2]])
		fname="t"+index[data[i].upper()[:-2]]+str(random.randint(100000,999999))
		f1 = open("/home/arsh/Dropbox/DATA_project_dataset_assembler_for_text_analysis/data_extraction_in_progress/charan_singh_arsh/"+fname+".txt", "w+")
		while data[j].upper()[:-2] not in index:
			if data[j]=="\n" and data[j+1]=="\n":
				j+=2
				flg=False
			elif data[j] == 'CHARAN SINGH: SELECTED SPEECHES \n':
				flg=True
				try:
					int(data[j+3][-3])
					j+=5
				except:
					j+=2
			else:
				if flg:
					f1.writelines(data[j])
				j+=1
			if j>=len(data):
				break
		f1.close()
	# f2 = open("/home/arsh/Dropbox/DATA_project_dataset_assembler_for_text_analysis/data_extraction_in_progress/"+"charan_singh_metadata.csv", "a")
	# writer = csv.writer(f2)
	# ctr+=1
	# speech_head=""
	# for t in data[i].lower():
	# 	if t.isalpha():
	# 		speech_head+=t
	# data_row = [fname,"charansingh", index[data[i].upper()[:-2]][:4],index[data[i].upper()[:-2]][:6], index[data[i].upper()[:-2]], "pmo", "firstterm","xxxxx" ,"" , "speech", "other", "other", "x", "india", "ncr", "newdelhi","capital", "hindiother", speech_head, "book", "x", index[data[i].upper()[:-2]][:4],"charan"+index[data[i].upper()[:-2]][:4], ctr, fname[-6:], "completed", "x", ctr, ctr ]
	# writer.writerow(data_row)
	# f2.close()	
	i=j