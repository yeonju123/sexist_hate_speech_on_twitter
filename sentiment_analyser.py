from collections import defaultdict
import csv
import konlpy
from konlpy.tag import Okt  
import pandas as pd
import os
import re


lexicon_dict = {}          # dictionary that will contain vocab as key and polairty value as its value.
dict_reader = csv.DictReader(open ("polarity.csv"))


for row in dict_reader:
   lexicon_dict.setdefault(row["ngram"],[ ]).append(row["max.value"])  #makes the values of ngram as the key that returns pos value. 


### classify vocab in the sentiment dictionary to each sentiment bag. ###


pos_bag = []
neg_bag = []
neut_bag = []
for key, _ in lexicon_dict.items():
   if lexicon_dict[key] == ["POS"]:
      pos_bag.append(str(key))
   elif lexicon_dict[key] == ["NEG"]:
      neg_bag.append(str(key))
   else:
      neut_bag.append(str(key))

   
###  This is the sentiment analyser function ###


def sentiment_analyser(handle):
   read_data = pd.read_csv(handle, sep = "\t")
   tokenized_tweets = read_data["tokenized_tweets"]
   splited_tweets = tokenized_tweets.str.split(",")
   for i in range(len(splited_tweets)):
      counter_pos = 0
      counter_neg = 0
      for word in splited_tweets[i]:
         word = re.sub(r"'", r"", word).strip()  
         if word in pos_bag:
            counter_pos += 1
            #print(word, "POS")
         elif word in neg_bag:
            counter_neg -= 1
            #print(word, "NEG")
         else:
            pass         
      read_data.loc[i,"pos_score"] = counter_pos
      read_data.loc[i,"neg_score"] = counter_neg
      read_data.loc[i,"total score"] = counter_pos + counter_neg
      #print(f"{i}th tweet",f"POS score: {counter_pos}", f"NEG score: {counter_neg}", f"Total:{counter_neg + counter_pos}")
      i+=1
   read_data.to_csv(input("The path to save the sentiment analysis(csv): "), index = False, sep = "\t", encoding = "utf-8")

   
### test support ###
read_data = pd.read_csv(handle, sep = "\t")
tokenized_tweets = read_data["tokenized_tweets"]
print(tokenized_tweets)
splited_tweets = tokenized_tweets.str.split(",")
splited_tweets[2601]









#----------------
os.getcwd()
lexicon_all = pd.read_csv('polarity.csv',sep=',')
lexicon_all.head(5)
lexicon_all.dtypes
lexicon_all_pos = lexicon_all[lexicon_all["max.value"]=="POS"]
lexicon_all_neg = lexicon_all[lexicon_all["max.value"]=="NEG"]

lexicon_all["max.value"].unique()
lexicon_all_neg["max.value"].unique()
lexicon_all_pos["max.value"].unique()


lexicon_all_pos.head()

data = pd.read_csv("cleaned_female.csv",sep='\t')
data.head()

tweetscorepos = []
tweetscoreneg = []

for tweets in data["tokenized_tweets"]:
   poscounter = 0
   negcounter = 0
   for ngram in lexicon_all_pos["ngram"]:
      if ngram in tweets:
         poscounter+=1
   for ngram in lexicon_all_neg["ngram"]:
      if ngram in tweets:
         negcounter-=1
   tweetscorepos.append(poscounter)
   tweetscoreneg.append(negcounter)


len(tweetscorepos)

datanew = pd.DataFrame()
datanew = pd.merge(data,pd.DataFrame(tweetscorepos,columns=['tweetscorepos']),left_index=True,right_index = True,how='left')
datanew = pd.merge(datanew,pd.DataFrame(tweetscoreneg,columns=['tweetscoreneg']),left_index=True,right_index = True,how='left')

datanew.tail()
datanew.dtypes

