from bs4 import BeautifulSoup
import requests
from random import randint
import time

def get_month(mo):
    op = ''
    if(mo == 'january'):
        op = '01'
    elif(mo == 'february'):
        op = '02'
    elif(mo == 'march'):
        op = '03'
    elif(mo == 'april'):
        op = '04'
    elif(mo == 'may'):
        op = '05'
    elif(mo == 'june'):
        op = '06'
    elif(mo == 'july'):
        op = '07'
    elif(mo == 'august'):
        op = '08'
    elif(mo == 'september'):
        op = '09'
    elif(mo == 'october'):
        op = '10'
    elif(mo == 'november'):
        op = '11'
    else:
        op = '12'
    return op

decade = ['2001-2010','liberation/2011-2020','liberation/2020/12/2021-2030']

for dec in decade:
    print('hi1')
    raw_years = requests.get("https://www.cpiml.net/"+dec)
    print('Going to sleep for 5 secs')
    time.sleep(5)
    print("Back, running")

    soup_year = BeautifulSoup(raw_years.text,'lxml')
    yrs = soup_year.find_all('nav',{'role' : 'navigation', 'aria-labelledby':"book-label-3"})
    
    yrl = [yr['href'] for yr in yrs[0].find_all('a',href = True)]
    

    for yr in yrl:
        curr_yr = yr[len(yr)-4:]
        month_page = requests.get("https://www.cpiml.net/"+yr)
        print('Going to sleep for 5 secs')
        time.sleep(5)
        print("Back, running")
        soup_month = BeautifulSoup(month_page.text,'lxml')
        month = soup_month.find_all('nav',{'role':'navigation','aria-labelledby':"book-label-3" })
        monthl = [mon['href'] for mon in month[0].find_all('a',href = True)]

        print('hi3')
        for mon in monthl:

            article_link_page = requests.get("https://www.cpiml.net/"+mon)
            print('Going to sleep for 5 secs')
            time.sleep(5)
            print("Back, running")
            soup_article_link = BeautifulSoup(article_link_page.text,'lxml')

            curr_mon = soup_article_link.find('h1',class_ = 'page-header').text
            curr_mon = curr_mon.replace(curr_yr,'')
            curr_mon = curr_mon.replace('-','')
            curr_mon = curr_mon.replace('\n','')
            articles = soup_article_link.find_all('nav',{'role':'navigation','aria-labelledby':"book-label-3" })
            
            articlel = [atc['href'] for atc in articles[0].find_all('a',href = True)]
            

            for article in articlel:
                art = requests.get("https://www.cpiml.net/"+article)
                print('Going to sleep for 5 secs')
                time.sleep(5)
                print("Back, running")
                soup_article = BeautifulSoup(art.text,'lxml')

                fs = soup_article.find('h1',class_ = 'page-header').text
                fs+= soup_article.find('div',class_ = "field field--name-body field--type-text-with-summary field--label-hidden field--item").text
                monstr = get_month(curr_mon.lower())
                id = 't'+curr_yr+monstr+'01'+str(randint(100000,999999))
                f = open('new_data/'+id+'.txt','w')
                f.write(fs.encode('utf-8'))
                f.close()