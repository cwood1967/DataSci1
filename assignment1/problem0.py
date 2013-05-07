'''
Created on May 5, 2013

@author: chris
'''

import urllib
import json

def gettweets(searchterm, page=None):
    url1 = "http://search.twitter.com/search.json?q="
    url = url1 + searchterm
    
    if page:
        url = url + "&page=" + str(page)
    
    print url 
    response = urllib.urlopen(url)
    return json.load(response)
    #the return is a dict


def getpages(searchterm, pages):
    npages = int(pages)
    tweetpages = []
    for i in xrange(npages):
        n = i + 1
        pagetweets = gettweets(searchterm, n)
        tweetpages.append(pagetweets)
        
def printtweets(tweets):
    results = tweets['results']
    for res in results:
        print res['text']
        
def getandprint(searchterm, pages = None):
    if pages is None:
        pages = 1
        
    for i in xrange(pages):
        pn = i +1
        print "*********************** Page " + str(pn) + "********************************"
        tweets = gettweets(searchterm, pn)
        printtweets(tweets)
        print "------------------------------------------------------------------------------"
        
        
        
    