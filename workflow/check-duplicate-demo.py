from urllib.request import urlopen
import re
import requests
import csv
from csv import writer
from bs4 import BeautifulSoup
import os
from random import randint, randrange

rows=[]



def find_duplicate(rows):
    uid=set()
    for i in range(1,len(rows)):
        if rows[i][0] not in uid:
            uid.add(rows[i][0])
        else:
            return True
        
    print('id lengths',len(uid))
    

    return False

def valid_id(rows):
    for i in range(1,len(rows)):
        if rows[i][0][0:3]!='t20':
            print('not valid')
            return False
        
    return True



with open('new_organizer.csv','r',encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        #print(row)
        if(len(row)!=0):
            rows.append(row)

#newrows=[]
#with open('i11.csv','r',encoding='utf-8') as f:
    #reader = csv.reader(f)
    #for row in reader:
        #print(row)
        #newrows.append(row)
            
print(len(rows), rows[1][0])
#print('length of new csv',len(newrows))

if(find_duplicate(rows)):
    print('Duplicates found')
else:
    print('No duplicates')


if(valid_id(rows)):
    print('IDs are valid')
else:
    print('IDs are not valid')
















