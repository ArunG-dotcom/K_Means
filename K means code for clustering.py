# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 17:00:55 2020

@author: reach
"""


#tsv is tab seperated value
# importing pandas random numpy unifrom
import pandas, random
import numpy as np
from random import uniform
import math






# main formula works for 300 dimensions



# Kmeans steps

# 1 step of Kmeans, initialize centroids
# main functions that can be used for inilitiazing centroids



# 2 step of Kmeans, identify the closest centroid to each data point



#Alpha_prime = []

#for i in range(15):
     #alpha = random.choice(clusters.T)
     #Alpha_prime += [list(alpha)]
     #print(Alpha_prime)
    
     
    
def check_datapoint_for_distance(datapoint1, centroids_location):
    #retern nearest cnetoird to datapoint
    datapoint1 = [np.linalg.norm(datapoint1, centroids_location)]
    return datapoint1



def group_datapoint(centroid_df, row):
    """groups datapoints together using distance function"""
    distance = math.inf
    index = int()
    
    for _, centroid in centroid_df.iterrows():
       
        d = np.linalg.norm(centroid - row)
        if d < distance:
            distance = d
            index = centroid.name
    return index



    
def reinitialize_centroids(clusters):
   clusters = clusters.groupby("group")
   clusters = clusters.mean() 
  
   
   
   return clusters
    
 
        
    

if __name__ == "__main__":
    
    #step1
    #Read the data and store into varaibles, defining variables
    #emoji = {}
    #with open( r"C:\Users\reach\OneDrive\Hello World\Helloworld\K means\emoji_lookup.tsv", encoding = "UTF-8") as f:
        #for line in f:
            #line = line.split("\t")
            #emoji["eoji" + line[0]] = line[1]
            
    # read files and use variables to be able to use them elsewhere
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
    #step2 
    #creating/intializing cnetroids
    centroids =  clusters.sample(k).reset_index(drop = True)
    print(clusters,centroids)
    clusters["group"] = clusters.apply(lambda row: group_datapoint(centroids, row), axis = 1)
    centroids =  reinitialize_centroids(clusters)
    print(clusters, centroids)
    
    
    clusters["group"] = clusters.apply(lambda row: group_datapoint(centroids, row), axis = 1)
    centroids =  reinitialize_centroids(clusters)
    
    print(clusters, centroids)
    
    for _ in range(15):
        
        clusters["group"] = clusters.apply(lambda row: group_datapoint(centroids, row), axis = 1)
        centroids =  reinitialize_centroids(clusters)
        print(clusters["group"].unique())
        print(centroids)
    
    clusters["emojiCode"] = emoji_Code
    #for group in range(15):
        #print(group)
        #series = clusters[clusters["group"] == group]["emojiCode"].tolist() # slicing clusters where column group is equal to group.
        #print(emoji[emoji["emojiCode"] in series]["symbol"])
        #for e in series:
            #print(emoji[e]) 
        #print("\n")
    clusters["symbol"] = emoji["symbol"]
    print(clusters)