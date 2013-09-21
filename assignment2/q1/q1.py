# -*- encoding: utf-8 -*-
from __future__ import unicode_literals
import requests
from requests_oauthlib import OAuth1
from urlparse import parse_qs
import json
REQUEST_TOKEN_URL = "https://api.twitter.com/oauth/request_token"
AUTHORIZE_URL = "https://api.twitter.com/oauth/authorize?oauth_token="
ACCESS_TOKEN_URL = "https://api.twitter.com/oauth/access_token"

CONSUMER_KEY = "r46KjjjIQmAISFZ0FdndQ"
CONSUMER_SECRET = "MEspj9D2kMLNXKwFKLly6DpxY4xHG5AknOR5aICZDA"

OAUTH_TOKEN = "299932017-9O6ezdFRELsq2XAjovKLrUkD7ISRS2KfPExqJSzf"
OAUTH_TOKEN_SECRET = "noxgwGKHAmSlKmgna1a5gYkIeHDE2kQYogrPCEDFIgs"


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
                   client_secret=CONSUMER_SECRET,
                   resource_owner_key=resource_owner_key,
                   resource_owner_secret=resource_owner_secret,
                   verifier=verifier)

    # Finally, Obtain the Access Token
    r = requests.post(url=ACCESS_TOKEN_URL, auth=oauth)
    credentials = parse_qs(r.content)
    token = credentials.get('oauth_token')[0]
    secret = credentials.get('oauth_token_secret')[0]

    return token, secret


def get_oauth():
    oauth = OAuth1(CONSUMER_KEY,
                client_secret=CONSUMER_SECRET,
                resource_owner_key=OAUTH_TOKEN,
                resource_owner_secret=OAUTH_TOKEN_SECRET)
    return oauth

if __name__ == "__main__":
    if not OAUTH_TOKEN:
        token, secret = setup_oauth()
        print "OAUTH_TOKEN: " + token
        print "OAUTH_TOKEN_SECRET: " + secret
        print
    else:
        oauth = get_oauth()
        urls = list()
        f = open('workfile', 'w')
        while len(urls) < 1001:
        ##first request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23python%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##first request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23ruby%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##first request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23python%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23csharp%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23javascript%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass

        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23go%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23cpp%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23html%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23go%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23less%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23sass%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23sinatra%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23school%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23rails%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23code%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23college%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass

        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23css%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23hacker%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23science%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23computer%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
        ##next request 
            r = requests.get(url="https://api.twitter.com/1.1/search/tweets.json?q=%23jobs%20filter%3Alinks&count=100&include_entities=true", auth=oauth)
            r = r.json()
            print r["search_metadata"]["count"] 
            for tweet in range(r["search_metadata"]["count"]):
                if ((r["statuses"][tweet])):
                    try: 
                        if (r["statuses"][tweet]["entities"]["urls"]!=[]):
                    # if tweet entities exists  
                             if(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"] not in urls):   
                        #if url already exists do not append                 
                                urls.append(r["statuses"][tweet]["entities"]["urls"][0]["expanded_url"])
                    except:
                        pass
            for links in urls:
                try:
                    f.write (links+"\n")
                except:
                    pass
            #pickle.dump(urls, workfile)
            #print len(urls)
