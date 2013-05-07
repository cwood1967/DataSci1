import sys
import json
import re

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
def calctext(text, sent_words):
    retext = re.sub("[^A-Za-z]"," ",text)
    words = retext.split()
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

def sentiment(fp, words):
    
    i = 0
    text = unicode("text")
    for line in fp.readlines():
        tweet = json.loads(line)
        
        try:
            tweettext = tweet[unicode('text')]
            score = calctext(tweettext, words)
        except Exception, e:
            #pass
            #print "Error", e, i
            score = 0
            
        print score
#         #if score < -15:print tweet
#         if i > 400:
#             break
#        i = i + 1
    
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    swords = getswords(sent_file)
    #print "Length of swords ", len(swords)
    #hw()
    #lines(sent_file)
    sentiment(tweet_file, swords)

if __name__ == '__main__':
    main()
