from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import urllib
import urllib.request
import time
import sys
import os
import random
import math
import pandas as pd

site= "https://a253013.sitemaphosting6.com/4227023/sitemap.xml"

#driver = webdriver.Firefox()
from selenium.webdriver import FirefoxOptions

opts = FirefoxOptions()
opts.add_argument("--headless")
driver = webdriver.Firefox(firefox_options=opts)

driver.get(site)
soup = BeautifulSoup(driver.page_source, 'html.parser')
div_tags = soup.find_all("div")
div=div_tags[1]
links=div.findAll("a")
urls=[]
for i in range(len(links)):
    a=str(links[i])
    i=a.find("https")
    j=a.rfind("https")
    b=a[i:j-2]
    urls.append(b)


ll=[]
for i in range(len(urls)):
    if urls[i].find("encyc")!=-1 or urls[i].find("Encyc")!=-1 or urls[i].find("archives")!=-1:
        
        ll.append(urls[i])
    
    else:
        pass

ll=ll[1:]
clean=[]
for i in range(len(ll)):
    if ll[i].find("archives")!=-1:
        if ll[i].find("page=") !=-1:
            clean.append(ll[i])
        else:
            pass
    else:
        clean.append(ll[i])
sites=[]
dates=[]
titles=[]
for i in range(len(clean)):
    if clean[i].find("encyc")!=-1 or clean[i].find("Encyc")!=-1:
        #date
        url=clean[i]
        s=clean[i].find('Encyc')
        if s==-1:
            t=clean[i].find('encyc')
            a=t+6
        else:
            a=s+6
            
        b=clean[i].rfind('/')
        date=url[a:b]
        #title
        c=url.rfind('/')+1
        d=url[c:]
        title=d[0:-5]
        
        sites.append(url)
        dates.append(date)
        titles.append(title)

dframe=pd.DataFrame(columns=["sites","dates","titles"])
dframe["sites"]=sites
dframe["dates"]=dates
dframe["titles"]=titles

matter=[]
for i in range(len(sites)):
    url=sites[i]
    driver = webdriver.Firefox()
    driver.get(url)
    obj = BeautifulSoup(driver.page_source, 'html.parser')
    driver.close()
    paras=obj.findAll("div", id="pastingspan1")
    paras=paras[2:]
    cp=""
    for i in range(len(paras)):
        a=str(paras[i]).strip('<div id="pastingspan1">')
        b=a.strip('</')
        cp=cp+b
    matter.append(cp) 

gdates=[]
for i in range(len(dates)):
    gdates.append(dates[i]+'g')

years=[]
months=[]
days=[]
for i in range(len(dates)):
    years.append(dates[i][0:4])
    a=dates[i].find("/")
    b=dates[i].rfind("/")
    months.append(dates[i][a+1:b])
    e=gdates[i].rfind("/")
    f=gdates[i].rfind("g")
    days.append(gdates[i][e+1:f])

doubles=['10','11','12']
m=[]
for i in range(len(months)):
    if months[i] in doubles:
        m.append(months[i])
    else:
        m.append('0'+months[i])
singles=['1','2','3','4','5','6','7','8','9']
d=[]
for i in range(len(days)):
    if days[i] in singles :
        d.append('0'+days[i])
        
    else:
        d.append(days[i])
code=[]
for i in range(len(years)):
    digits = [i for i in range(0, 10)]
    random_str = ""
    for i in range(6):
        index = math.floor(random.random() * 10)
        random_str += str(digits[index])
    code.append(random_str)

for i in range(len(years)):
    with open('t{}{}{}{}.txt'.format(years[i],m[i],d[i],code[i]),'w') as f:
        f.write(dates[i])
        f.write('\n')
        f.write('\n')
        f.write(titles[i])
        f.write('\n')
        f.write('\n')
        f.write(matter[i])