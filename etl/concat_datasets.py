'''
This code is for the first day of the challenge - Data Cleaning and Preparation

Concatenate all datasets in raw folder in just one for future cleaning
'''

# Imports
import pandas as pd
import numpy as np
import os

# Path for raw data
path = 'data\\raw'

# List all files in folder
files = [os.path.join(path, f) for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]

# Array for storing the DataFrames
dataframes = []

# Reading all files of raw folder and save them in dataframes
for file in files:
    df = pd.read_csv(file, sep=';', skiprows=1, encoding='latin1')
    dataframes.append(df)

# Concat all DataFrames in just one
concat_data = pd.concat(dataframes, ignore_index=True)

# Save concat_data in raw folder
concat_data.to_csv('data\\raw\\despesa_ceaps_2008-2022.csv', index=False)
