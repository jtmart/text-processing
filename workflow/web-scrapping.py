#extracting tags

#importing libraries for extracting tags
from urllib.request import urlopen
import re
import requests
from bs4 import BeautifulSoup
import csv
from csv import writer

#assigning main url which contains all source links
url = "https://organiser.org/sitemap_index.xml" #main url
page = urlopen(url) #opening the url page
html_bytes = page.read() #reading page data
html = html_bytes.decode("utf-8") #getting html data of the url
#print((html))

request = requests.get(url) #requesst made on url
Soup = BeautifulSoup(request.text, 'lxml') #processing html text file for getting all tags data using BeautifulSoub library

listurl=[] #contains list of all source url

# creating a list of data under loc tags
heading_tags = ["loc"] #definig particular tag under which we want to collect data

for tags in Soup.find_all(heading_tags): #run loop for finding data under particular tag in all html page data
    listurl.append(tags.text.strip()) #add all source url data under particular url in list
    #print(tags.name + ' -> ' + tags.text.strip()) #printing data as output for particular tag

src_url_date=[] #contains list of all last modified date of particular tag in url 
src_url_time=[] #contains list of all last modified time of particular tag in url 

heading_tags = ["lastmod"] #definig particular tag under which we want to collect data

for tags in Soup.find_all(heading_tags): #run loop for finding data under particular tag in all html page data
    string=str(tags.text.strip()) #converting data to string
    src_url_date.append(string[:10]) #slicing the string data for extracting last modified date under particular url
    src_url_time.append(string[11:16]) #slicing the string data for extracting last modified time under particular url
    #print(tags.name + ' -> ' + tags.text.strip()) #printing data under particular tag

count=[] #list for appending no. of tags under particular source url

with open('organizer.csv', 'a') as f_object: #open the new file for appending data
  
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
  
            # Difining list of column along with the name for csv file to append data
            List=["UNIQUE ID","SOURCE URL","SOURCE URL DATE","SOURCE URL TIME","CORRESPONDING URL","CORRESPONDING URL DATE","CORRESPONDING URL TIME"]
            # Pass the list as an argument into the writerow()
            writer_object.writerow(List)
  
            #Close the file object
            f_object.close()
            
########################################################
#code block to append all sub links under particular source link
for index in range(0,46): #defing range of source url till which we want to collect data
    newurl=listurl[index] #getting particular source url for finding its all sub links
    print(newurl) #printing respective source url

    page = urlopen(newurl) #opening the url page
    html_bytes = page.read() #reading page data
    html = html_bytes.decode("utf-8") #getting html data of the url

    newrequest = requests.get(newurl) #requesst made on url
    newSoup = BeautifulSoup(newrequest.text, 'lxml') #processing html text file for getting all tags data using BeautifulSoub library
    #print((html))

    dest_url_date=[] #contains list of all last modified date of particular tag in sub url 
    dest_url_time=[] #contains list of all last modified time of particular tag in sub url
    heading_tags = ["lastmod"] #definig particular tag under which we want to collect data

    for tags in newSoup.find_all(heading_tags): #run loop for finding data under particular tag in all html page data
      string=str(tags.text.strip()) #converting data to string
      dest_url_date.append(string[:10]) #slicing the string data for extracting last modified date under particular url
      dest_url_time.append(string[11:16]) #slicing the string data for extracting last modified time under particular url

    newlisturl=[] #contains list of all sub urls under source url
    heading_tags = ["loc"] #definig particular tag under which we want to collect data
    for tags in newSoup.find_all(heading_tags): #run loop for finding data under particular tag in all html page data
        newlisturl.append(tags.text.strip()) #add all sub url data under particular url in list
        

    for idx in range(len(newlisturl)): #lop for appending the all data in csv file
        with open('organizer.csv', 'a') as f_object:  #open the new file for appending data
  
            # Pass this file object to csv.writer()
            # and get a writer object
            writer_object = writer(f_object)
  
            # Difining list of column along with the name for csv file to append data
            List=[index+1,newurl,src_url_date[index],src_url_time[index],newlisturl[idx],dest_url_date[idx],dest_url_time[idx]]
            # Pass the list as an argument into the writerow()
            writer_object.writerow(List)
            
            #Close the file object
            f_object.close()
    

    count.append(len(newlisturl)) #appending the count of total url under particular source url
    print("No. of sub urls in above url", len(newlisturl)) #priting no. of sub urls under particular source url
    
