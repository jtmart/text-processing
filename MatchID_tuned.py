import os
import re
import pandas as pd

folder_name=['loksabha']

Members = pd.read_csv('loksabha.csv', sep=',', index_col=False, encoding='iso-8859-1')
count=0
Verdict=[]
j=0
a=0
falseout = 0

for i in range(len(folder_name)):
	j+=1
	Files = []
	PathMain = str(folder_name[i])
	print(PathMain)
	for (dirpath, dirnames, filenames) in os.walk(PathMain):
		Files.extend(filenames)
		break

	IDs = []

	Verdict = []

	for Row in range(len(Members)):
		CID = Members.loc[Members.index[Row],'id']
		IDs.append(CID)

	for File in Files:
		FileName = File[:len(File)-4]
		a+=1
		if FileName in IDs:
			Verdict.append('True for '+FileName)
		else:
			Verdict.append('False for '+FileName)
			print('Error at '+FileName)
			falseout +=1
	count+=len(Verdict)
	#with open('false_output.txt','w',encoding='utf-8') as f:
	#	f.write('\n'.join(Verdict))
print('Files Checked - ',a)
print('Verdict Found - ',count)
print('Folders Checked - ',j)
print('Error in Files - ',falseout)