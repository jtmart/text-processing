encoding='utf-8'

import csv
import os
from collections import defaultdict
# from datetime import time
# dict_pm={}
# dict_pm=dict(defaultdict(list))
# #dict_pm---> different categories: dict_pm['nmo_spe']---->list of ids whose text files I need. 


# with open('metadata_cleanonly.csv', 'r', encoding='utf-8') as f:  #or encoding='utf-8' or 'latin-1' or 'iso-8859-1' or 'mac_roman'
#     reader = csv.reader(f)
#     data = list(reader)
# ctr=0
# for i in data[171:]:  #column numer 2 in the csv will be noted 1 in here. Pick the column to group by and change lines below accordingly.
#     # print(i[0], i[171])
#     ctr+=1
#     if (ctr%1000==0):
#         print (ctr)
#     if i[1] not in dict_pm:
#         dict_pm[i[171]]=""
#     with open(f'beta1_2_essential_f/{i[0]}.txt', 'r', encoding='utf-8') as f:
#         text= f.read()
#     #dict_pm[i[171]]= dict_pm[i[171]] + text + " "
#     dict_pm[i[171]].append(text+" ")

# for key in dict_pm.keys():
#     with open(f'experiment/{key}.txt', "w", encoding='utf-8') as outfile:  #create folder "combined" beforehand, or "os.makedirs('combined')" to create one
#         outfile.write(dict_pm[key])


# start=time.time()

with open('metadata_cleanonly.csv', 'r', encoding='utf-8') as f:  #or encoding='utf-8' or 'latin-1' or 'iso-8859-1' or 'mac_roman'
    reader = csv.reader(f)
    data = list(reader)
ctr=0
dict_pm=dict()
for i in data[1:]:
    # print (i)  #column numer 2 in the csv will be noted 1 in here. Pick the column to group by and change lines below accordingly.
    # print(i[0], i[171])
    ctr+=1
    if (ctr%10000==0):
        print (ctr)
    if i[171] not in dict_pm:
        dict_pm[i[171]]=""
    with open(f'beta1_2_essential_f/{i[0]}.txt', 'r', encoding='utf-8') as f:
        text= f.read()
    #dict_pm[i[171]]= dict_pm[i[171]] + text + " "
    dict_pm[i[171]]=dict_pm[i[171]]+text+" "
    # if (ctr%10000==0):
    #     print (i[171], dict_pm[i[171]])
# print (time.time()-start)
for key in dict_pm.keys():
    with open(f'experiment/{key}.txt', "w", encoding='utf-8') as outfile:  #create folder "combined" beforehand, or "os.makedirs('combined')" to create one
        outfile.write(dict_pm[key])
