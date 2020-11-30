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

# -----------------------------------------------------------------------------
# scrape tweets with keywords
df = GET_TWEETS(api=api, 
                str_search_words="#prestige OR #prestigefinance OR #prestigefinancialservices", 
                str_date_since='2019-11-03', 
                int_n_tweets=2500, 
                int_n_rounds=6)

# -----------------------------------------------------------------------------
import pandas as pd

# state the account name
str_account_id = 'AllUtahHomes'

# get number of followers
int_n_followers = api.get_user(str_account_id).followers_count

# get all followers of the account
followers = api.followers(id=str_account_id,
                          count=200) # entered 200 because it maxes out

# get the screen name and date followed account for each follower
df_empty = pd.DataFrame()
# iterate through followers
for follower in followers:
    # only get those in UT
    if ('UT' in follower.location) or ('utah' in follower.location.lower()):
        # create dictionary
        dict_ = {'screen_name': follower.screen_name,
                 'location': follower.location}
        # append to df_empyy
        df_empty = df_empty.append(dict_, ignore_index=True)





    




    