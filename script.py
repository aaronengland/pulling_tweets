# scraping tweets
import os
# change dir
os.chdir('M:\\Risk Management\\AaronE_scripts\\17_pulling_tweets\\pulling_tweets')
from scripts.functions import CONNECT_TO_TWITTER, GET_TWEETS
from twitter_dev_credentials import API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# connect to API
api = CONNECT_TO_TWITTER(API_KEY, 
                         API_KEY_SECRET, 
                         ACCESS_TOKEN, 
                         ACCESS_TOKEN_SECRET)

# scrape tweets with keywords
df = GET_TWEETS(api=api, 
                str_search_words="#prestige OR #prestigefinance OR #prestigefinancialservices", 
                str_date_since='2019-11-03', 
                int_n_tweets=2500, 
                int_n_rounds=6)









    




    