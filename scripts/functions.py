# functions
import tweepy as tw

# define function to connect to twitter API
def CONNECT_TO_TWITTER(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET):
	# pass twitter credentials to tweepy via its OAuthHandler
	auth = tw.OAuthHandler(API_KEY, API_KEY_SECRET)
	auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
	api = tw.API(auth, wait_on_rate_limit=True)
	# return
	return api