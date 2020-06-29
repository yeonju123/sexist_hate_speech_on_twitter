import csv
import os
import re
import nltk
import pandas as pd

os.getcwd()

          
df_year_dict = {}
all_men_df = pd.DataFrame()                      

for i in range(10, 19):                         #automates reading all files
    uncleaned_data = f"male_20{i}_91_1130.csv"
    df_year_dict[f"20{i}"]= pd.read_csv(uncleaned_data, header=None).assign(year = f"20{i}") #"tag" all read tweets with a written year and update into a dictionary
    i+=1


all_men_df = pd.concat(df_year_dict, axis=0, ignore_index = True)      #integrates all read files into a single dataframe
all_men_df['cleaned_tweets'] = all_men_df[0].str.replace(r"<.*?>",r"")   #removes html stuff by replacing it to a blank, leaving tweets only.
all_men_df['cleaned_tweets'].str.strip()
#print(all_men_df['cleaned_tweets'].str.replace(r"\s+", r"__"))
all_men_df.drop([0], axis = 1, inplace = True )                           #removes the raw data read via csv from the columns of the dataframe 


all_men_df.drop_duplicates('cleaned_tweets', inplace = True)    #drop duplicates in data.
all_men_df.to_csv("cleaned_male_2010_18.csv", index = False, sep = "\t", encoding = "utf-8")  #writes the created dataframe containing cleaned tweets into a new csv file.

#for x in all_men_df["year"]:    #chekcs whether the data is located under the correct header.
 #   assert x.isdigit()