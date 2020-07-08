import os
import csv

path="C:\\Users\\jtmartelli\\Google Drive\\2017_Drive\\Modi\\Test_python_script3\\corpus"
#Make sure you dont have any other files in this folder other than the ones mentioned in Renaming_file.csv

with open('Renaming_file.csv', 'r') as f:
    reader = csv.reader(f)
    names = list(reader)
print (names)
for i in range(len(names)):
    if(i==0):
        continue
    print (names[i][0],names[i][1])
    os.rename(path+'/'+names[i][0]+'.txt',path+'/'+names[i][1]+'.txt')
