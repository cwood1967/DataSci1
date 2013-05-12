import sys
import json
import re
import traceback

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))
    
    
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

def sentiment(fp, words):
    terms = {}    
    i = 0
    text = unicode("text")
    for line in fp.readlines():
        tweet = json.loads(line)
        
        try:
            tweetraw = tweet[unicode('text')]
            #print tweetraw
            tweettext = re.sub("[^A-Za-z\'@]"," ",tweetraw)
            #tweettext = tweettext.lower()
            score = calctext(tweettext, words)
            tweetterms = tweettext.split()
            nterms = float(len(tweetterms))
            for term in tweetterms:
                if words.has_key(term):
                    continue
                if terms.has_key(term):
                    terms[term].append(score/nterms)
                else:
                    terms[term]= [score]
                    
        except Exception, e:
            pass
            #print tweet
            score = 0
#
#         if score > 0:
#             for t in terms.keys():
#                 print t,terms[t]
#             i +=  1
#         if i > 7:break
        i = i + 1
   
    for term in terms.keys():
        scores = terms[term]
        num = len(scores)
        avg = sum(scores)/float(num)
        print term, avg
        
    #print len(terms)
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    swords = getswords(sent_file)
    sentiment(tweet_file, swords)

if __name__ == '__main__':
    main()
