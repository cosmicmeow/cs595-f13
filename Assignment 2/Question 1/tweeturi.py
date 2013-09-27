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

terms_array = ['bread', 'coffee', 'cake', 'macaron', 'macarons', 'croissant', 
               'tfiosmovie', 'html', 'java', 'python', 'javascript', 'hashtag', 
               'github', 'css', 'mojang', 'naughtydog', 'steamos', 'steammachine', 
               'valve', 'cfa', 'acm', 'odu', 'netflix', 'breakingbad', 'gta5']


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


def search(oauth, links_list):
    for term in terms_array:
        r = requests.get(url='https://api.twitter.com/1.1/search/tweets.json?q=' + term + '&filter%3Alinks&count=1000', auth = oauth)
        for status in r.json()['statuses']:
            for url in status['entities']['urls']:
                if len(links_list) == 1000:
                    return
                if 'expanded_url' in url:
                    uri = url['expanded_url']
                    try:
                        r = requests.get(uri)
                        if r.status_code == 200 and not r.url in links_list:
                            links_list.add(r.url)
                            print('Added uri: ' + r.url + ' #' + str(len(links_list)))
                    except requests.exceptions.ConnectionError as e:
                        continue
                    except UnicodeEncodeError as e:
                        continue
                    except IOError as e:
                        continue

def search_hashtags(oauth, links_list):
    for term in terms_array:
        r = requests.get(url='https://api.twitter.com/1.1/search/tweets.json?q=%28' + term + '&filter%3Alinks&count=1000', auth = oauth)
        for status in r.json()['statuses']:
            for url in status['entities']['urls']:
                if len(links_list) == 1000:
                    return
                if 'expanded_url' in url:
                    uri = url['expanded_url']
                    try:
                        r = requests.get(uri)
                        if r.status_code == 200 and not r.url in links_list:
                            links_list.add(r.url)
                            print('Added uri: ' + r.url + ' #' + str(len(links_list)))
                    except requests.exceptions.ConnectionError as e:
                        continue
                    except UnicodeEncodeError as e:
                        continue
                    except IOError as e:
                        continue


if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()
        links_list = set()
        search(oauth, links_list)
        search_hashtags(oauth, links_list)
        print(links_list)

        file = open('twitter_links.txt', 'w')
        for item in links_list:
            file.write("%s\n" % item)