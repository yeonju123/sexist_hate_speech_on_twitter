# coding: utf-8

import matplotlib.pyplot as plt
import datetime
from matplotlib.dates import YearLocator, MonthLocator, DateFormatter
import pandas as pd


# count the frequency of the misogyny and misandry word by year.


reader = pd.read_csv("/Users/yeonjulee/Downloads/python project 2/sentiment_analyzed_male.csv", sep = "\t", encoding = "utf-8")
reader.index
reader.loc[0, "total score"]

counter10 = 0 
counter11 = 0 
counter12 = 0 
counter13 = 0 
counter14 = 0 
counter15 = 0 
counter16 = 0 
counter17 = 0
counter18 = 0

reader.loc[400, "year"]


reader.index
for i in range(2602):
    if reader.loc[i, "total score"] <= 0:
        if str(reader.loc[i, "year"]) == "2010":
            counter10 += 1
        elif str(reader.loc[i, "year"]) == "2011":
            counter11 += 1
        elif str(reader.loc[i, "year"]) == "2012":
            counter12 += 1
        elif str(reader.loc[i, "year"]) == "2013":
            counter13 += 1
        elif str(reader.loc[i, "year"]) == "2014":
            counter14 += 1
        elif str(reader.loc[i, "year"]) == "2015":
            counter15 += 1
        elif str(reader.loc[i, "year"]) == "2016":
            counter16 += 1
        elif str(reader.loc[i, "year"]) == "2017":
            counter17 += 1
        elif str(reader.loc[i, "year"]) == "2018":
            counter18 += 1

print(f"2010: {counter10} 2011: {counter11}, 2012: {counter12}, 2013: {counter13}, 2014:{counter14}, 2015:{counter15}, 2016: {counter16} 2017:{counter17}, 2018:{counter18}")
count_freq = [counter10, counter11, counter12, counter13, counter14, counter15, counter16, counter17, counter18]


df = pd.DataFrame({"female_freq": count_freq})
df.to_csv("frequency_result.csv", sep = "\t", encoding = "utf-8")
df["male_freq"] = count_freq
df.to_csv("frequency_result.csv", sep = "\t", encoding = "utf-8")


# draw a plot based on the result obtained above.

reader = pd.read_csv("/Users/yeonjulee/Downloads/python project 2/frequency_result.csv", sep = "\t")  #read the file that the result is saved
malelist = reader["male_freq"].tolist()
femalelist = reader["female_freq"].tolist()
year = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]


plt.plot(year, malelist, "b--", label = "han-nam")
plt.plot(year, femalelist, "r--", label = "kimch-nye")
plt.xticks(range(2010,2019))
plt.legend(loc='upper center')
plt.grid(True)
plt.savefig("freq_result.png")

plt.show()


