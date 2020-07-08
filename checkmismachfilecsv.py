import csv
import os
import shutil

files=os.listdir('/home/lirus/Documents/DataExtract-master/Renamed_Files')
files=[f.rstrip('.txt') for f in files]

#os.makedirs('NEW_FILES')
print(files)

data=[]
not_found=[]
with open('/home/lirus/Documents/DataExtract-master/Final_RAJIV_3.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        if(row[0]=='id'):
            continue
        if(row[0] in files):
            data.append(row)
            files.remove(row[0])
            #shutil.copyfile('FILES/{}.txt'.format(row[0]),'NEW_FILES/{}.txt'.format(row[0]))
        else:
            not_found.append(data)

print(len(data))
print(len(not_found))
print(files)
'''
with open ('FIXED.csv','w') as f:
    writer = csv.writer(f)
    writer.writerows(data)
'''
