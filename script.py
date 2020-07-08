# import os
# import numpy as np 
# import pandas as pd 
# from youtube_transcript_api import YouTubeTranscriptApi
# filename=pd.read_csv("bk_shivani.txt")
# filename=filename.to_numpy()

# for i in range (len(filename)):
# 	filename[i][0]=filename[i][0][32:]

# unusable_link=""
# for i in range (len (filename)):
# 	video_id=filename[i][0]
# 	try:

# 		transcript_list=YouTubeTranscriptApi.get_transcript(video_id)
# 		s=""
# 		for j in range (len (transcript_list)):
# 			s+=" "+ transcript_list[j]['text']+'\n'
# 		text_name=str(i+1)+"_bk_shivani.txt"
# 		text_file=open (text_name, 'w+')
# 		text_file.write(s)
# 		text_file.close()
# 	except:
# 		print (i)
# 		links="https://www.youtube.com/watch?v="+video_id+'\n'
# 		print (links)
# 		unusable_link+=links

# print (unusable_link)
# link=open("bad_links.txt", 'w+')
# link.write(unusable_link)
# link.close()


import requests
from bs4 import BeautifulSoup as bs # importing BeautifulSoup

# sample youtube video url
# video_url ="https://www.youtube.com/watch?v=65grVv1tzss"
video_url="https://www.youtube.com/watch?v=jNQXAC9IVRw"
# get the html content
content = requests.get(video_url)
# create bs object to parse HTML
soup = bs(content.content, "html.parser")
# write all HTML code into a file
open("video.html", "w", encoding='utf8').write(content.text)
