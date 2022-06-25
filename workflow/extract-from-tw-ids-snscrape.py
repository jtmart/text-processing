import snscrape.modules.twitter as twitterScraper
import json
import csv
from csv import writer
import pandas as pd


def writetext(name,fs):
    f = open('extract/'+name+'.txt','w',encoding='utf-8')
    f.write(fs)
    f.close()

    
rows=[]
with open('influencers.csv','r',encoding="utf8") as f:
    reader = csv.reader(f)
    for row in reader:
        rows.append(row)


tweets=[]
for j in range(1,len(rows)):
  str = rows[j][4]
  print(j)
  scraper = twitterScraper.TwitterSearchScraper('from:%s'%str)
  try:
      
      for i,tweet in enumerate(scraper.get_items()):
        tweets.append([rows[j][1],tweet.id, tweet.content, tweet.user.username])
        
        
  except:
      print("Exception Catch2")
      continue
    
    #tweets.append([rows[j][1],tweet.id, tweet.content, tweet.user.username])
    #print([rows[j][1],tweet.id, tweet.content, tweet.user.username])
    
with open('new.csv', 'a') as f_object:
  writer_object = writer(f_object)
  List=["STR_ID","USERNAME","UNIQUE ID","TWEETS"]
  writer_object.writerow(List)
  f_object.close()


for idx in range(0,len(tweets)):
  with open('new.csv', 'a',encoding="utf8") as f_object:
    writer_object = writer(f_object)
    List=[tweets[idx][0],tweets[idx][3],tweets[idx][1],tweets[idx][2]]
    st=tweets[idx][1]
    writetext('%s'%st,tweets[idx][2])
    writer_object.writerow(List)
    f_object.close()


