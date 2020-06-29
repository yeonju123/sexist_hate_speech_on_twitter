import pandas as pd
import os
from konlpy.tag import Mecab
mecab = Mecab()


os.getcwd()

def csv_reader(handle, result_h):
    print("start")                 #handle = path of the relevant file.
    csv_read = pd.read_csv(filepath_or_buffer = handle , sep = "\t")
    print("start1")
    #csv_read["tokenized_okt_tweets"] = csv_read["cleaned_tweets"].apply(lambda x: okt.pos(x, norm = True, stem = True, join = True)) # pos tagging with stems, not influcted version, and with the tag joined.
    csv_read["tokenized_tweets"] = csv_read["cleaned_tweets"].apply(lambda x: mecab.pos(x, join = True))  #pos tagging with normalizing only.
    print("midway through")    
    csv_read.assign(tokenized = csv_read["tokenized_tweets"])
    print("almost")
    csv_read.to_csv(result_h, index = False, sep = "\t", encoding = "utf-8" ) #tokenizing and saving into the existing file.
    print("done")
    #print(csv_read)

handle = "cleaned_male_2010_18.csv"
result_h = "met_pos_cleaned_male_2010_18_.csv"

csv_reader(handle, result_h)



