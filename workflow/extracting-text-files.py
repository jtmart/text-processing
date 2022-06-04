from urllib.request import urlopen
import re
import requests
import csv
from csv import writer
from bs4 import BeautifulSoup
import os
from random import randint, randrange

rows=[]
date=[]
nos=[]
uqid=[]

def find(arr):
    string="t"
    num=randint(100000,999999)
    if num not in nos:
        nos.append(num)
        for i in arr:
            string+=i
    string+=str(num)    
            
    return string


def writetext(name,fs):
    uqid.append(name)
    f = open('extract/'+name+'.txt','w',encoding='utf-8')
    f.write(fs)
    f.close()
    

with open('organizer.csv','r') as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)

demo=[]
bodylist=[]
headinglist=[]

def heading(soup):
  for tags in soup:
      #print(tags.text.strip(),i)
      hd=tags.text.strip()
  headinglist.append(hd)



for row in range(1,len(rows)):

    if(len(rows[row])!=0):

        arr=rows[row][5].split('-')
        request = urlopen(rows[row][4])
        Soup = BeautifulSoup(request.read(), "html.parser")
        
        fs = Soup.find('div',class_ = "content-inner")
        writetext(find(arr),fs.text)

        heading_tags = ["h1"]
        head=Soup.find_all(heading_tags)
        heading(head)
        



with open('new.csv', 'a') as f_object:
  
            writer_object = writer(f_object)
            List=["UNIQUE ID","SOURCE URL","SOURCE URL DATE","SOURCE URL TIME","CORRESPONDING URL","CORRESPONDING URL DATE","CORRESPONDING URL TIME","CORRESPONDING URL TITLE"]
            writer_object.writerow(List)
            f_object.close()


print('lengths',len(headinglist),len(uqid))


for idx in range(0,len(rows)-1):

        with open('new.csv', 'a') as f_object:
  
            writer_object = writer(f_object)
            List=[uqid[idx],rows[idx+1][1],rows[idx+1][2],rows[idx+1][3],rows[idx+1][4],rows[idx+1][5],rows[idx+1][6],headinglist[idx]]
            writer_object.writerow(List)
            f_object.close()




    
