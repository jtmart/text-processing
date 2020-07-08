import os.path
from apiclient.discovery import build 
import pprint 
import pandas as pd
# api_key= AIzaSyAdgHHmUHVlrS-TGB97Lq1Y0LcPAqEE11g
# arguments to be passed to build function 
DEVELOPER_KEY = "AIzaSyAdgHHmUHVlrS-TGB97Lq1Y0LcPAqEE11g"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
# creating youtube resource object 
# for interacting with API 
youtube = build(YOUTUBE_API_SERVICE_NAME,YOUTUBE_API_VERSION, developerKey = DEVELOPER_KEY) 

def video_details(video_id): 
	list_videos_byid = youtube.videos().list(id = video_id, part = "id, snippet, contentDetails, statistics").execute() 
	results = list_videos_byid.get("items", []) 
	for result in results: 
		return (result["snippet"]["publishedAt"])


# punc=list()
# for i in range (975):
# 	filename=str(i)+"_bk_shivani.txt"
# 	if (os.path.isfile(filename)):
# 		with open(filename, 'r') as myfile:
# 			data = myfile.read()
# 		c=data.count('.')
# 		if (c==0):
# 			punc.append([filename, "No"])
# 			# print (data)
# 		else:
# 			punc.append([filename, "Yes"])

# import numpy as np
# punc=np.array(punc)
# np.savetxt("punctuation.txt", punc, delimiter=",", fmt='%s')


from youtube_transcript_api import YouTubeTranscriptApi
filename=pd.read_csv("bk_shivani.txt")
filename=filename.to_numpy()


for i in range (len(filename)):
	filename[i][0]=filename[i][0][32:]
for i in range (len (filename)):
	video_id=filename[i][0]
	found=False
	try:

		transcript_list=YouTubeTranscriptApi.get_transcript(video_id)
		found=True
	except:
		found=False
	if (found==True):
		date=video_details(video_id)
		date=date[:10]
		date=date[:4]+date[5:7]+date[8:10]
		if (i%10==0):
			print (date)
