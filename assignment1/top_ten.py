'''
Created on May 8, 2013

@author: chris
'''

import sys
import json
import re
import traceback
import operator

def hw():
    print 'Hello, world!'

# def lines(fp):
#     print str(len(fp.readlines()))
    
    
def calctext(text, sent_words):
    #retext = re.sub("[^A-Za-z]"," ",text)
    words = text.split()
    score = 0
    for word in words:
        try:
            a = sent_words[word]
            #print word, a
        except:
            #print word, " not found"
            a = 0
        score = score + a
    #print "Final Score: ", score   
    return score
def getswords(file):
    words = {}
    for line in file:
        s = line.split("\t")
        try:
            phrase = s[0]
            words[phrase] = int(s[1])
        except Exception, e:
            pass
            #print e, s[0], s[1]
    return words

def topten(fp):
    dont = re.compile(r'(http)|(#)')
    #dont.append( [unicode("#")])
    #dont.append( [unicode("https")])

    terms = {}    
    i = 0
    text = unicode("text")
    hashtagdict = {}
    for line in fp.readlines():
        tweet = json.loads(line)
        try:
            hashtags = tweet["entities"]['hashtags']
            for tag in hashtags:
                text = tag['text']
                #print text
                if text in hashtagdict.keys():
                    hashtagdict[text] += 1
                else:
                    hashtagdict[text] = 1
                    
                #print text, hashtagdict[text]
        except Exception, e:
            #print "What happened", e
            pass
        

    m = sorted(hashtagdict.items(), key=lambda item: item[1])
        
    m.reverse()
    for i in range(10):
       print m[i][0], float(m[i][1])
       
    
def main():
    tweet_file = open(sys.argv[1])
    topten(tweet_file)

if __name__ == '__main__':
    main()

