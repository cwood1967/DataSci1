'''
Created on May 8, 2013

@author: chris
'''

import sys
import json
import re
import traceback

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

def frequency(fp):
    dont = re.compile(r'(http)|(#)')
    #dont.append( [unicode("#")])
    #dont.append( [unicode("https")])

    terms = {}    
    i = 0
    text = unicode("text")
    for line in fp.readlines():
        tweet = json.loads(line)
        
        try:
            tweetraw = tweet[unicode('text')]
            tweettext = tweetraw.lower()
            #score = calctext(tweettext, words)
            tweetterms = tweettext.split()
            nterms = float(len(tweetterms))
            for term in tweetterms:
                if dont.search(term):
                    #print "************", term, tweetraw
                    continue
                term = re.sub("[^0-9A-Za-z\']","",term)
                if term == "":
                    continue
                if terms.has_key(term):
                    terms[term] += 1
                else:
                    terms[term]= 1
                #print term,terms[term]
        except Exception, e:
            pass
            #print "error ", e
            #print tweet
            #score = 0
#
#         if score > 0:
#             for t in terms.keys():
#                 print t,terms[t]
#             i +=  1
#         if i > 7:break
        i = i + 1
    for term in terms.keys():
        print term, terms[term]
        
    #print len(terms)
def main():
    tweet_file = open(sys.argv[1])
    frequency(tweet_file)

if __name__ == '__main__':
    main()
