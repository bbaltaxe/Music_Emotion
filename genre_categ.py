# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 22:24:34 2019

@author: marco
"""

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#importing the dataset
dataset = pd.read_csv('metadata_2014.csv')

# take all the lines and all the columns except for the last one
X = dataset.iloc[:, 0:5]  #.value
#data_X = pd.DataFrame(X)

# Split the genres except for Hip-Hop using a RegEx
splitted = X["Genre"].str.split("-(?!Ho)", n = 15, expand = True)

# Select the unique genres after the splitted table
genres = splitted.apply(pd.value_counts)
genres['genre'] = genres.index

# Create a dictionary with the different genres
# and for each genre append a column to the dataset
dict = {}

for key, val in enumerate(genres['genre']):
    dict[key] = val
    X[val] = pd.Series(0, index=X.index)
    

def findValues(gen):
    tempCol = []
    for cell in X['Genre']:
        if cell.find(gen) != -1:
            tempCol.append(1)
        else:
            tempCol.append(0)
    return tempCol

for gen in dict.values():
    tempCol = findValues(gen)
    X.loc[:, gen] = tempCol
    
         


