# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs

REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "azgp8wM0twPByZDT3lbFOg"
CONSUMER_SECRET = "oVRsknjLZxGORayDonnFUhbtpeIwRqojRI7bfhQkA"

OAUTH_TOKEN = "1225949790-xEaSD8KAIbXSaOGvlxlWHW7Ju8oe0UfuRZiN4vg"
OAUTH_TOKEN_SECRET = "MYVCjq7jxmcJe07rN1yTr2c0KTALAZxdpgBeYf7eC4"

def setup_oauth():
    """Authorize your app via identifier."""
    # Request token
    oauth = OAuth1(CONSUMER_KEY, client_secret=CONSUMER_SECRET)
    r = requests.post(url=REQUEST_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)

    resource_owner_key = credentials.get('oauth_token')[0]
    resource_owner_secret = credentials.get('oauth_token_secret')[0]

    # Authorize
    authorize_url = AUTHORIZE_URL + resource_owner_key
    print 'Please go here and authorize: ' + authorize_url

    verifier = raw_input('Please input the verifier: ')
    oauth = OAuth1(CONSUMER_KEY,
                   client_secret = CONSUMER_SECRET,
                   resource_owner_key = resource_owner_key,
                   resource_owner_secret = resource_owner_secret,
                   verifier = verifier )

    # Finally, Obtain the Access Token
    r = requests.post(url = ACCESS_TOKEN_URL, auth = oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret = CONSUMER_SECRET,
                resource_owner_key = OAUTH_TOKEN,
                resource_owner_secret = OAUTH_TOKEN_SECRET)
    return oauth



if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()

        outfile = open('paradox_twitter_FC.txt', 'w')
        r = requests.get(url='https://api.twitter.com/1.1/followers/list.json?cursor=-1&count=200&screen_name=' + 'cosmic_meow', auth = oauth)

        followers_count = 0

        for persons in r.json()['users']:
        	username = str(persons['screen_name'])
        	followers = str(persons['followers_count'])
        	print (username + ',' + followers)
        	outfile.write(username + ',' + followers + '\n')
        	followers_count = followers_count +1

outfile.write('cosmic_meow,' + str(followers_count))
outfile.close()

