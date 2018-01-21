
# coding: utf-8

# ## Tweepy Twitter Frontend for Octogen

# In[1]:

import tweepy
from values import *
# setup
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# make api obj
api = tweepy.API(auth)


# In[2]:

# get_filename
def send_tweet(file):
	tweet = "Made with OctoGAN @GitHubEducation #MyOctocat #sbhacks #makewaves"
	return api.update_with_media(file, status = tweet)


