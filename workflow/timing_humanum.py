import snscrape.modules.twitter as twitterScraper
from tqdm import tqdm
import time
import pandas as pd
from helper import *
import os

def writetext(name,fs):
    f = open('extract/'+name+'.txt','w',encoding='utf-8')
    f.write(fs)
    f.close()


def extract(row):
    limit=None # DONT FORGET THIS!!!

    start_time = time.time()
    user_name = row[4]
    scraper = twitterScraper.TwitterSearchScraper('from:%s'%user_name)

    # create dataframe for the user
    tweets = pd.DataFrame(columns=["str_id", "tweet_id", "username", "tweet_date", "tweet_content", "num_comments", "num_likes", "num_retweets"])

    # iterate over all the tweets made by the user and append them to the dataframe
    for i,tweet in enumerate(scraper.get_items()):
        try:
            tweets = tweets.append({
                "str_id": row[1],
                "tweet_id": tweet.id,
                "username": tweet.user.username,
                "tweet_date": tweet.date,
                "tweet_content": tweet.content,
                "num_comments": tweet.quoteCount, 
                "num_likes": tweet.likeCount, 
                "num_retweets": tweet.retweetCount
            }, ignore_index=True)
        except Exception as e:
            print(f"Exception occured at {i} for username: {user_name}")

        if limit is not None and i == limit:
            break
            
    print(f"CSV for username: {user_name} saved")
    tweets.to_csv(f"./files/{user_name}.csv", index=False) # DONT FORGET THIS!!!

    with open("timings.txt", "a") as timefile:
        timefile.write("%s,%s\n" % (str, time.time() - start_time))
        timefile.close()
    return tweets


if __name__ == "__main__":
    final_dataframe = pd.DataFrame(columns=["str_id", "tweet_id", "username", "tweet_date", "tweet_content"])
    df = pd.read_csv("influencers.csv").to_numpy()[:]

    list_of_df = map_parallel(extract, df, workers=5, graph=False)
    
    print("All extraction finished, deleting the backup files...")
    for filename in tqdm(os.listdir("./files")):
        os.remove(f"./files/{filename}")
    
    print("Merging the dataframes")
    for temp in tqdm(list_of_df):
        final_dataframe = final_dataframe.append(temp)

    final_dataframe.reset_index(drop=True).to_csv("./all_tweets.csv", index=False)
