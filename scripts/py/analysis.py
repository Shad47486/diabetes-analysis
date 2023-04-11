import pandas as pd
import numpy as np 

df = pd.read_csv("C:/Users/Shad/.pyenv/PProjects/diabetes-analysis/data/diabetic_data.csv")


## Looking to see how many dublicates ##
duplicate_encounters = df.duplicated(subset='patient_nbr', keep=False).sum()
print(f"Number of duplicate patient encounters: {duplicate_encounters}")
# number of duplicate encounters = 47021 
## meaning there was a total of 94042 encounter ##


## looking to see how many of those patients where duplicates
duplicate_counts = df.duplicated(subset='patient_nbr', keep=False).groupby(df['patient_nbr']).sum().reset_index(name='count')
print(duplicate_counts)
# 1 = >30, 2 = <30 (see DD for details)
duplicate_counts = duplicate_counts[(df.duplicated(subset='patient_nbr', keep=False)) & (df['readmitted'].isin(['1', '2']))]
# Sort the dataframe in descending order of counts
duplicate_counts = duplicate_counts.sort_values(by='count', ascending=False)
print("Top 10 patients with the most readmissions:")
print(duplicate_counts.head(10))