'''
Created on Apr 26, 2018

@author: ribrahim
'''

import tweepy
from tweepy import OAuthHandler
import config

consumer_key = config.consumer_key
consumer_secret = config.consumer_secret
access_token = config.access_token
access_secret = config.access_secret

auth = OauthHandler(consumer_key, consumer_secret)
auth.set_acces_toke(access_token, access_secret)

apit = tweepy.Api(auth)