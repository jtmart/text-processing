#-*- coding: utf-8 -*-
import csv
from bs4 import BeautifulSoup
#import urllib.request
from subprocess import call
#import pyperclip
from textblob import TextBlob
import numpy as np
import collections

filename='metadata2.csv'

string=' '
count=0

with open(filename, 'rb') as f:
    reader = csv.reader(f)
    #your_list = list(reader)

counter=1
simp=0
with open(filename,'r') as f:
    reader = csv.reader(f)
    for row in reader: #For skipping the first row i.e. the one which contains the variable names
        if(count==0):
            count=1
            continue
        temp='**** '
        #print (len(row))
        columns=len(row)
        for i in range (0,columns):
            if(row[i]==' ' or row[i]==''):
                row[i]='x'
            temp=temp+'*var{}_'.format(i+1)+str(row[i])+' '
        #print row[0]
        #fi = open('corpus/{}.txt'.format(your_list[counter][0]), 'rb')
        fi = open('corpus/{}.txt'.format(row[0]), 'rb')
        counter+=1
        #print (fi.read())
        try:
            string=string+temp+'\n'+fi.read().decode("utf-8") +'\n'
        except:
            print ("latin")
            simp+=1
            string=string+temp+'\n'+fi.read().decode("latin-1") +'\n'


f=open('concat2.txt','w', encoding="utf-8")
f.write(string)
print (simp)
