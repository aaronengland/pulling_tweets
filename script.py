# scraping tweets
import os
# change dir
os.chdir('M:\\Risk Management\\AaronE_scripts\\17_pulling_tweets\\pulling_tweets')
from scripts.functions import *
from twitter_dev_credentials import *
import pandas as pd

# connect to API
api = CONNECT_TO_TWITTER(API_KEY, 
                         API_KEY_SECRET, 
                         ACCESS_TOKEN, 
                         ACCESS_TOKEN_SECRET)

str_search_words = "#prestige OR #prestigefinance OR #prestigefinancialservices"
str_date_since = "2019-11-03"
int_n_tweets = 100





# define function to get all the tweets we can
def GET_TWEETS(api, str_search_words, str_date_since, int_n_tweets=2500, int_n_rounds=6):
    # start timer
    time_start = time.perf_counter()
    
    # create empty df we will eventually return
    df_empty_return = pd.DataFrame()
    
    # pull tweets at each round of tweet collection
    for a in range(int_n_rounds):
        # print message
        print('Scraping round {a+1} of {int_n_runs} tweets.')
        # get the tweets as an iterable object
        iter_tweets = tw.Cursor(api.search, 
                                q=str_search_words, 
                                lang='en', 
                                since=str_date_since, 
                                tweet_mode='extended').items(int_n_tweets)
        # create empty df
        df_empty = pd.DataFrame()
        # iterate through iter_tweets and get the info we want
        for tweet in iter_tweets:
            # create dictionary
            dict_ = {'handle_name': tweet.user.screen_name,
                     'date': tweet.created_at,
                     'location': tweet.user.location,
                     'n_followers': tweet.user.followers_count,
                     'text': tweet.full_text}
            # append to df_empty
            df_empty = df_empty.append(dict_, ignore_index=True)
        # concatenate df_empty to df_empty_return
        df_empty_return = pd.concat([df_empty_return, df_empty])
        # pause function for 15 minutes to prevent lockout if we are not on the last round
        if a < (int_n_rounds - 1):
            # print message
            print('Pausing tweet collection for 15 min. to prevent lockout.')
            # pause function for 15 minutes to prevent lockout if we are not on the last round
            time.sleep(900)
    # print message of total time elapsed
    print(f'Tweet collection complete; Total time elapsed: {(time.perf_counter()-time_start)/60:0.4} min.')
    # return
    return df_empty_return
    




    program_start = time.time()
    for i in range(0, numRuns):
        # We will time how long it takes to scrape tweets for each run:
        start_run = time.time()
        
        # Collect tweets using the Cursor object
        # .Cursor() returns an object that you can iterate or loop over to access the data collected.
        # Each item in the iterator has various attributes that you can access to get information about each tweet
        tweets = tweepy.Cursor(api.search, q=search_words, lang="en", since=date_since, tweet_mode='extended').items(numTweets)
# Store these tweets into a python list
        tweet_list = [tweet for tweet in tweets]
# Obtain the following info (methods to call them out):
        # user.screen_name - twitter handle
        # user.description - description of account
        # user.location - where is he tweeting from
        # user.friends_count - no. of other users that user is following (following)
        # user.followers_count - no. of other users who are following this user (followers)
        # user.statuses_count - total tweets by user
        # user.created_at - when the user account was created
        # created_at - when the tweet was created
        # retweet_count - no. of retweets
        # (deprecated) user.favourites_count - probably total no. of tweets that is favourited by user
        # retweeted_status.full_text - full text of the tweet
        # tweet.entities['hashtags'] - hashtags in the tweet
# Begin scraping the tweets individually:
        noTweets = 0
for tweet in tweet_list:
# Pull the values
            username = tweet.user.screen_name
            acctdesc = tweet.user.description
            location = tweet.user.location
            following = tweet.user.friends_count
            followers = tweet.user.followers_count
            totaltweets = tweet.user.statuses_count
            usercreatedts = tweet.user.created_at
            tweetcreatedts = tweet.created_at
            retweetcount = tweet.retweet_count
            hashtags = tweet.entities['hashtags']
try:
                text = tweet.retweeted_status.full_text
            except AttributeError:  # Not a Retweet
                text = tweet.full_text
# Add the 11 variables to the empty list - ith_tweet:
            ith_tweet = [username, acctdesc, location, following, followers, totaltweets,
                         usercreatedts, tweetcreatedts, retweetcount, text, hashtags]
# Append to dataframe - db_tweets
            db_tweets.loc[len(db_tweets)] = ith_tweet
# increase counter - noTweets  
            noTweets += 1
        
        # Run ended:
        end_run = time.time()
        duration_run = round((end_run-start_run)/60, 2)
        
        print('no. of tweets scraped for run {} is {}'.format(i + 1, noTweets))
        print('time take for {} run to complete is {} mins'.format(i+1, duration_run))
        
        time.sleep(920) #15 minute sleep time
# Once all runs have completed, save them to a single csv file:
    from datetime import datetime
    
    # Obtain timestamp in a readable format
    to_csv_timestamp = datetime.today().strftime('%Y%m%d_%H%M%S')
# Define working path and filename
    path = os.getcwd()
    filename = path + '/data/' + to_csv_timestamp + '_sahkprotests_tweets.csv'
# Store dataframe in csv with creation date timestamp
    db_tweets.to_csv(filename, index = False)
    
    program_end = time.time()
    print('Scraping has completed!')
    print('Total time taken to scrap is {} minutes.'.format(round(program_end - program_start)/60, 2))