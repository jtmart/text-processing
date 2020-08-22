import os
import re
import pandas as pd

LS = pd.read_csv('Metadata_LS.csv', sep=',', index_col=False)
count = 0
Verdict = []
j = 0
a = 0
falseout = 0

Files = []
PathMain = "TextFiles"
print(PathMain)
for (dirpath, dirnames, filenames) in os.walk(PathMain):
	Files.extend(filenames)
	break

IDs = []
IDsDict = {}

NotFoundID = []
NotFoundFile = []
NewFiles = []
NewFilesDict = {}

for Row in range(len(LS)):
	CID = LS.loc[LS.index[Row],'id']
	IDs.append(CID)
	try:
		IDsDict[CID]+= 1
		NotFoundID.append(CID)
	except KeyError:
		IDsDict[CID]=1

print('Number of Files:',len(Files))
print('Number of IDs:',len(IDs))

for File in Files:
	FileName = File[:len(File)-4]
	NewFiles.append(FileName)
	try:
		NewFilesDict[FileName]+= 1
		NotFoundFile.append(FileName)
	except KeyError:
		NewFilesDict[FileName]=1
	#if FileName not in IDsDict.keys():
	#	NotFoundFile.append(FileName)

#for ID in IDs:
#	if ID not in NewFilesDict.keys():
#		NotFoundID.append(ID)

print('Files Checked:',len(NewFiles))
print('IDs Checked:',len(IDs))
print('IDs Not Found:',len(NotFoundID))
print('Files Not Found:',len(NotFoundFile))
print(NotFoundID)
print(NotFoundFile)