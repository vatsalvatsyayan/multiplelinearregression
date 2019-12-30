# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#We first import Libraries 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Now we will import the dataset press F5 before executing the following

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:,:-1]
y = dataset.iloc[:,4]

#Convert the column into categorical columns

states = pd.get_dummies(x['State'],drop_first=True)

# Drop the State colimn

X = X.drop('State',axis=1)

