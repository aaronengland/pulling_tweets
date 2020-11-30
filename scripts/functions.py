# functions
import tweepy as tw
import time
import pandas as pd

# define function to connect to twitter API
def CONNECT_TO_TWITTER(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
	# pass twitter credentials to tweepy via its OAuthHandler
	auth = tw.OAuthHandler(API_KEY, API_KEY_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tw.API(auth, wait_on_rate_limit=True)
	# return
	return api

# define function to get all the tweets we can
def GET_TWEETS(api, str_search_words, str_date_since, int_n_tweets=2500, int_n_rounds=6):
	# start timer
	time_start = time.perf_counter()

	# create empty df we will eventually return
	df_empty_return = pd.DataFrame()

	# pull tweets at each round of tweet collection
	for a in range(int_n_rounds):
		# print message
		print(f'Scraping round {a+1} of {int_n_rounds} tweets.')
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