import tweepy as tw 
import configparser as cf
import pandas as pd

config= cf.ConfigParser()
config.read('config.ini')

api_key= config['twitter']['api_key']
api_key_secret= config['twitter']['api_key_secret']
access_token= config['twitter']['access_token']
access_token_secret= config['twitter']['access_token_secret']

auth=tw.OAuthHandler(api_key,api_key_secret)
auth.set_access_token(access_token,access_token_secret)

api=tw.API(auth)


##Get tweets from home page

public_tweets=api.home_timeline()

data=[]
for tweet in public_tweets:
  data.append([tweet.created_at,tweet.user.screen_name,tweet.text])


tweets_df=pd.DataFrame(data,columns=(['Time','User','Tweet']))
print(tweets_df.head())

tweets_df.to_csv('Tweets-HomePage.csv')

##Get tweets of a spcific user

user='Sentdex'
limit=100

user_tweets=api.user_timeline(screen_name=user,count=limit,tweet_mode='extended')

data1=[]
for tweet in user_tweets:
  data1.append([tweet.user.screen_name,tweet.full_text])
  
usertweets_df=pd.DataFrame(data1,columns=['User','Tweet'])
print(usertweets_df.head())

usertweets_df.to_csv('usertweets.csv')

##Get tweets of a specific hashtag

keyword='covid19'
limit=100

keyword_tweets=api.search_tweets(q=keyword,count=limit,tweet_mode='extended')
data2=[]

for tweet in keyword_tweets:
  data2.append([tweet.user.screen_name,tweet.full_text])

keywordtweets_df=pd.DataFrame(data2,columns=['User','Tweet'])
print(keywordtweets_df.head())

keywordtweets_df.to_csv('keywordtweet.csv')




