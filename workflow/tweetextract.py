#pip3 install git+https://github.com/JustAnotherArchivist/snscrape.git
#run this in command first
#boolean possibe... e.g. for i,tweet in enumerate(sntwitter.TwitterSearchScraper('@jtmartelli OR @vihanjumle since:2021-02-09 until:2021-02-10').get_items()):
#Just note that this script appends new results to an existing sheet

import snscrape.modules.twitter as sntwitter
import csv
maxTweets = 3000000

#keyword = '#ModiStrikesBack'
#place = '5e02a0f0d91c76d2' #This geo_place string corresponds to İstanbul, Turkey on twitter.
#keyword = 'covid'
#place = '01fbe706f872cb32' This geo_place string corresponds to Washington DC on twitter.

#Open/create a file to append data to
csvFile = open('AG_#ArrestAllInstigators_09_11_20022021.csv', 'a', newline='', encoding='utf8')

tweet_list = []

#Use csv writer
csvWriter = csv.writer(csvFile)
csvWriter.writerow(['Username','date','Tweet','Tweet_ID','Retweets','Likes','Quotes', 'Replies','Source','Location', 'Created_on','Followers']) 

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('#ModiStrikesBack since:2021-02-09 until:2021-02-10').get_items()):
        if i > maxTweets :
            break  
        csvWriter.writerow([tweet.user.username, tweet.date, tweet.content, tweet.id, tweet.retweetCount, tweet.likeCount, tweet.quoteCount, tweet.replyCount, tweet.source, tweet.user.location, tweet.user.created, tweet.user.followersCount])
csvFile.close()