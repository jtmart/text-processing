from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from get_data import get_all_valid_links
import time
from random import randint
from bs4 import BeautifulSoup


all_valid_links = get_all_valid_links()
driver = webdriver.Chrome()
cnt = 0
for link in all_valid_links:
    print(link)
    print(cnt)
    cnt+=1
    driver.get(link)
    ps = driver.page_source
    bp = BeautifulSoup(ps,'lxml')
    fs = ''
    try:
        fs+= bp.find('h1',class_ = 'page-header').text
    except:
        pass
    try:
        fs+= bp.find('div',class_ = "field field--name-body field--type-text-with-summary field--label-hidden field--item").text
    except:
        pass
    yr = link[29:33]
    mo = link[34:36]
    id = 't'+yr+mo+'01'+str(randint(100000,999999))
    f = open('new_data/'+id+'.txt','w')
    f.write(fs)
    f.close()

driver.close()