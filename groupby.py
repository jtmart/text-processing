encoding='utf-8'

import csv
import os

dict_pm={}

with open('corpus/metadata.csv', 'r', encoding='utf-8') as f:  #or encoding='utf-8' or 'latin-1' or 'iso-8859-1' or 'mac_roman'
    reader = csv.reader(f)
    data = list(reader)

for i in data[1:]:  #column numer 2 in the csv will be noted 1 in here. Pick the column to group by and change lines below accordingly.
    print(i[0], i[1])
    if i[1] not in dict_pm:
        dict_pm[i[1]]=""
    with open(f'corpus/{i[0]}.txt', 'r') as f:
        text= f.read()
    dict_pm[i[1]]= dict_pm[i[1]] + text + " "

for key in dict_pm.keys():
    with open(f'combined/{key}.txt', "w") as outfile:  #create folder "combined" beforehand, or "os.makedirs('combined')" to create one
        outfile.write(dict_pm[key])