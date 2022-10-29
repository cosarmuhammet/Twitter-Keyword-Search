# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 14:32:08 2022

@author: Mc
"""

import tweepy
import configparser
import pandas as pd

# read configs
config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)



# search tweets
keywords = '@HAVELSANResmi'
limit=300

tweets = tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode='extended').items(limit)



# create DataFrame
#columns = ['Time','User', 'Tweet']
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    
    #data.append([tweet.user.created_at, tweet.user.screen_name, tweet.full_text])
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)


#df.to_excel(r'HavelsanResmeTWEET.xlsx', index = False)
df.to_csv('HavelsanResmeTWEET.csv')
#print(df)


#xlsx to csv dönüştürme
#read_file = pd.read_excel (r'HavelsanResmeTWEET.xlsx')
#read_file.to_csv (r'HavelsanResmeTWEET.csv', index = None, header=True)






