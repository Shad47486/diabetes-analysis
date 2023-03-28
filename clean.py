import pandas as pd
import numpy as np 

#importing dataset
data = pd.read_csv('data/diabetic_data.csv')
#looking at each column for any data types that may need changing to help with analysis
data.columns
data.dtypes
df = data

#dropping all Columns not involved in analysis (wight, payercode, examide, citoglipton)
#see DD for reason why
data = data.drop(columns=['weight','payer_code', 'examide', 'citoglipton'])
data.info()
#race 
#Assigned each distinct value with a numerical value (See DD for changes)
#Categorical-nominal
race_list = {'?': 0, 
             'AfricanAmerican': 1, 
             'Asian': 2,
             'Caucasian': 3,
             'Hispanic': 4,
             'Other': 5}
data['race'] = data['race'].map(race_list)
print(data.race)

#gender
#Assigned Female/Male Unknown/invalid as 0,1,2 respectfully
#Categorical-nominal
gender_list = {'Unknown/Invalid': 0,
               'Female': 1,
               'Male': 2}
data['gender'] = data['gender'].map(gender_list)
gender_count = data['gender'].value_counts()
print(data.gender)

#age
#Assigned each group as a numerical Value, for example: 0-10 = 1 and the ones going on 90-100 = 10
age_list = {'[0-10)': 1, 
            '[10-20)': 2, 
            '[20-30)': 3, 
            '[30-40)': 4, 
            '[40-50)': 5, 
            '[50-60)': 6, 
            '[60-70)': 7, 
            '[70-80)': 8, 
            '[80-90)': 9, 
            '[90-100)': 10}
data['age'] = data['age'].map(age_list)

#medical_Speciality
#Assigned Each distinct value as a numerical number based on alphabetical order
Med_list = {'?': 0,
            'AllergyandImmunology': 1,
            'Anesthesiology': 2,
            'Anesthesiology-Pediatric': 3,
            'Cardiology': 4,
            'Cardiology-Pediatric': 5,
            'DCPTEAM': 6,
            'Dentistry': 7,
            'Dermatology': 8,
            'Emergency/Trauma': 9,
            'Endocrinology': 10,
            'Endocrinology-Metabolism': 11,
            'Family/GeneralPractice': 12,
            'Gastroenterology': 13,
            'Gynecology': 14,
            'Hematology': 15,
            'Hematology/Oncology': 16,
            'Hospitalist': 17,
            'InfectiousDiseases': 18,
            'InternalMedicine': 19,
            'Nephrology': 20,
            'Neurology': 21,
            'Neurophysiology': 22,
            'Obsterics&Gynecology-GynecologicOnco': 23,
            'Obstetrics': 24,
            'ObstetricsandGynecology': 25,
            'Oncology': 26,
            'Ophthalmology': 27,
            'Orthopedics': 28,
            'Orthopedics-Reconstructive': 29,
            'Osteopath': 30,
            'Otolaryngology': 31,
            'OutreachServices': 32,
            'Pathology': 33,
            'Pediatrics': 34,
            'Pediatrics-AllergyandImmunology': 35,
            'Pediatrics-CriticalCare': 36,
            'Pediatrics-EmergencyMedicine': 37,
            'Pediatrics-Endocrinology': 38,
            'Pediatrics-Hematology-Oncology': 39,
            'Pediatrics-InfectiousDiseases': 40,
            'Pediatrics-Neurology': 41,
            'Pediatrics-Pulmonology': 42,
            'Perinatology': 43,
            'PhysicalMedicineandRehabilitation': 44,
            'PhysicianNotFound': 45,
            'Podiatry': 46,
            'Proctology': 47,
            'Psychiatry': 48,
            'Psychiatry-Addictive': 49,
            'Psychiatry-Child/Adolescent': 50,
            'Psychology': 51,
            'Pulmonology': 52,
            'Radiologist': 53,
            'Radiology': 54,
            'Resident': 55,
            'Rheumatology': 56,
            'Speech': 57,
            'SportsMedicine': 58,
            'Surgeon': 59,
            'Surgery-Cardiovascular': 60,
            'Surgery-Cardiovascular/Thoracic': 61,
            'Surgery-Colon&Rectal': 62,
            'Surgery-General': 63,
            'Surgery-Maxillofacial': 64,
            'Surgery-Neuro': 65,
            'Surgery-Pediatric': 66,
            'Surgery-Plastic': 67,
            'Surgery-PlasticwithinHeadandNeck': 68,
            'Surgery-Thoracic': 69,
            'Surgery-Vascular': 70,
            'SurgicalSpecialty': 71,
            'Urology': 72}
data['medical_specialty'] = data['medical_specialty'].map(Med_list)
print(data['medical_specialty'])

### PATIENTS health Measurements ######
#See DD for data information, Units, and any changes made
#Max_glu_serum
max_list = {'None': 0,
            'Norm': 140,
            '>200': 200,
            '>300': 300}
data['max_glu_serum'] = data['max_glu_serum'].map(max_list)
print(data['max_glu_serum'])

#A1Cresult
a1c_list = {'None': 0, 
            'Norm': 4.5, 
            '>7': 7, 
            '>8': 8}
data['A1Cresult'] = data['A1Cresult'].map(a1c_list)

#Metformin 
metformin_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['metformin'] = data['metformin'].map(metformin_list)

#Repaglinide
repaglinide_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['repaglinide'] = data['repaglinide'].map(repaglinide_list)

#Nateglinide
nateglinide_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['nateglinide'] = data['nateglinide'].map(nateglinide_list)

#Chlorpropamide
chlorpropamide_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['chlorpropamide'] = data['chlorpropamide'].map(chlorpropamide_list)

#Glimepiride
glimepiride_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['glimepiride'] = data['glimepiride'].map(glimepiride_list)

#Acetohexamide
acetohexamide_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['acetohexamide'] = data['acetohexamide'].map(acetohexamide_list)

#Glipizide
glipizide_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['glipizide'] = data['glipizide'].map(glipizide_list)

#Glyburide
glyburide_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['glyburide'] = data['glyburide'].map(glyburide_list)

#Tolbutamide
tolbutamide_list = {'No': 0, 
                    'Steady': 1}
data['tolbutamide'] = data['tolbutamide'].map(tolbutamide_list)

#Pioglitazone
pioglitazone_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['pioglitazone'] = data['pioglitazone'].map(pioglitazone_list)

#Rosiglitazone
rosiglitazone_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['rosiglitazone'] = data['rosiglitazone'].map(rosiglitazone_list)

#Acarbose
acarbose_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['acarbose'] = data['acarbose'].map(acarbose_list)

#Miglitol
miglitol_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['miglitol'] = data['miglitol'].map(miglitol_list)

#Troglitazone
troglitazone_list = {'No': 0, 
                     'Steady': 1}
data['troglitazone'] = data['troglitazone'].map(troglitazone_list)

#Tolazamide
tolazamide_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['tolazamide'] = data['tolazamide'].map(tolazamide_list)

#Insulin
insulin_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['insulin'] = data['insulin'].map(insulin_list)

#Glyburide-metformin
glyburide_metformin_list = {'No': 0, 
                  'Steady': 2, 
                  'Up': 3, 
                  'Down': 1}
data['glyburide-metformin'] = data['glyburide-metformin'].map(glyburide_metformin_list)

#Glipizide-metformin
glipizide_metformin_list = {'No': 0, 
                            'Steady': 1}
data['glipizide-metformin'] = data['glipizide-metformin'].map(glipizide_metformin_list)

#Glimepiride-pioglitazone
glimepiride_pioglitazone_list = {'No': 0, 
                                 'Steady': 1}
data['glimepiride-pioglitazone'] = data['glimepiride-pioglitazone'].map(glimepiride_pioglitazone_list)

#Metformin-rosiglitazone
metformin_rosiglitazone_list = {'No': 0, 
                                'Steady': 1}
data['metformin-rosiglitazone'] = data['metformin-rosiglitazone'].map(metformin_rosiglitazone_list)

#Metformin-pioglitazone
metformin_pioglitazone_list = {'No': 0, 
                               'Steady': 1}
data['metformin-pioglitazone'] = data['metformin-pioglitazone'].map(metformin_pioglitazone_list)

#Change
change_list = {'No': 0, 
               'Ch': 1}
data['change'] = data['change'].map(change_list)

#DiabetesMed
diabetesmed_list = {'No': 0, 'Yes': 1}
data['diabetesMed'] = data['diabetesMed'].map(diabetesmed_list)

#Readmitted
readmitted_list = {'NO': 0, '>30': 1, '<30': 2}
data['readmitted'] = data['readmitted'].map(readmitted_list)

#looking to see if fields are in the correct data type
data.info()
#changed a1c into int after being float
data['A1Cresult'] = data['A1Cresult'].astype('Int64')



#saves data
data.to_csv('data/cleandata.csv') 