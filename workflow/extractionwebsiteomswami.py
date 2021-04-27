import requests
from bs4 import BeautifulSoup
from random import randint


def make_link(st):
    stn = st.lower().split(' ')
    r = ''
    for wd in stn:
        r+=wd+'-'
    return r[:len(r)-1]

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

def get_right_date(ls):
    for stobj in ls:
        st = stobj.text
        try:
            stn = st.split(' ')
            moind = len(stn)-3
            yrind = len(stn)-1
            dayind = len(stn)-2
            mo = stn[moind]
            day = stn[dayind][:len(stn[dayind])-1]
            yr = stn[yrind][:len(stn[yrind])-1]
            if(len(day)==1):
                day = '0'+day
            mo = get_month(mo.lower())

            try:
                k = int(mo)
                m = int(yr)
            except:
                continue
            break
        except:
            pass
    return yr+mo+day
    


for i in range(1,31):
    print('Page = ',i)
    main_page_link = 'https://os.me/wisdom/page/'+str(i)+'/'
    raw_page = requests.get(main_page_link)
    soup_page = BeautifulSoup(raw_page.text,'lxml')
    sub_links = soup_page.find_all('h6',class_= 'card-title')
    links = []
    for ele in sub_links:
        z = ele.find('a',href = True)
        links.append(z['href'])

    for link in links:
        final_str = ''
        article = requests.get(link)
        soup_ar = BeautifulSoup(article.text,'lxml')
        title = soup_ar.h1.text

        final_str+=title + '\n'
        sub_heading = soup_ar.find('p',class_ = 'headline small').text
        final_str+=sub_heading


        content = soup_ar.find('div',class_ = 'post-content').text
        final_str+=content
        #print(final_str)


        date = soup_ar.find_all('div', class_ = "col-sm-6")
        right_date = get_right_date(date)
        id = "t"+right_date+str(randint(100000,999999))

        f = open('/Users/harkishansingh/Desktop/intern_JT/omswami-ongoing/new_data_harkishan/'+id+".txt",'w') 
        f.write(final_str)
        f.close()
        