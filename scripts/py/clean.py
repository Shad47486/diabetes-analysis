import pandas as pd
import numpy as np 

df = pd.read_csv("C:/Users/Shad/.pyenv/PProjects/diabetes-analysis/data/diabetic_data.csv")

#### Removing duplicate encounters > 2 
#### patients that came more >2 times bc, may cause confounding factors 
#### aka affects the independent and dependent variables ####

# Count the number of encounters for each patient
#encounter_counts = df['patient_nbr'].value_counts()
# Get the list of patient IDs with more than 2 encounters
#patient_ids_to_remove = encounter_counts[encounter_counts > 2].index.tolist()
# Remove all encounters for patients with more than 2 encounters
#df = df[~df['patient_nbr'].isin(patient_ids_to_remove)]
#print(df)


### removing rows of patients that had a discharge_disposition_id
### these rows have
# Define the list of discharge IDs to remove
# Define a list of values to remove
to_remove = [11, 13, 14, 19, 20, 21]
df = df[~df['discharge_disposition_id'].isin(to_remove)]
### removeing the not needed columns and the first row that was created
to_remove2 = ['?']
df = df[~df['race'].isin(to_remove2)]
to_remove3 = ['Unknown/Invalid']
df = df[~df['gender'].isin(to_remove3)]
df = df.drop(columns=['weight','payer_code', 'examide', 'citoglipton', 'metformin-rosiglitazone', 'metformin-pioglitazone', 'acetohexamide'])
print(df)
df.dtypes
df.to_csv('C:/Users/Shad/.pyenv/PProjects/diabetes-analysis/data/cleandatav3.csv')