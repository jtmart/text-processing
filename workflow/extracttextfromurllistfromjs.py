import urllib.request 
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup 

# here we have to pass url and path 
# (where you want to save ur text file) 
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
links=open("03jan2010.txt", "r",encoding="utf-8")
lines= links.readlines()
count=0
for line in lines:
	line = line.replace('\n','')
	reg_url=line
	#reg_url = "https://www.organiser.org/archives/dynamic/modules968d.html?name=Content&pa=showpage&pid=407&page=2"
	req = Request(url=reg_url, headers=headers) 
	html = urlopen(req).read() 
	soup = BeautifulSoup(html, 'html.parser') 
	file_name="txt"+str(count)+".txt"
	f = open(file_name, "w",encoding="utf-8") 
	  
	# traverse paragraphs from soup 
	for data in soup.find_all("p"): 
	    sum = data.get_text() 
	    f.writelines(sum) 
	  
	f.close()
	count+=1
#print(html) 

# file = open("txt.txt", "r") 
# contents = file.read() 
# '''soup = BeautifulSoup(contents, 'html.parser') 

# f = open("test1.txt", "w") 

# # traverse paragraphs from soup 
# for data in soup.find_all("p"): 
# 	sum = data.get_text() 
# 	f.writelines(sum) 