# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 15:28:52 2020

@author: reach
"""

from sklearn.cluster import KMeans
import pandas

emoji = pandas.read_csv(
    r"C:\Users\reach\OneDrive\Hello World\Helloworld\K means\emoji_lookup.tsv",
    delimiter = '\t',
    names = ["emojiCode", "symbol"]
        )

    #print(emoji)
    # read dataframe same as csv for clusters

clusters = pandas.read_csv(
        r"C:\Users\reach\OneDrive\Hello World\Helloworld\K means\clusters.txt",
        delimiter= ' '
        )
emoji_Code = clusters["emojiCode"]
clusters.drop('emojiCode', axis = 1, inplace = True)
    
clusters = clusters.astype(float)
k = 15 # clusters - is 15
kmeans = KMeans(n_clusters=15)
clusters["group"] = kmeans.fit_predict(clusters)

clusters["emojiCode"] = emoji_Code

clusters["symbol"] = emoji["symbol"]

for i in range(15):
   ls = clusters[clusters["group"] == i]["symbol"].to_list()
   print(f'for the group{i} the emojis are{ls} \n')