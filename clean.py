import pandas as pd
import numpy as np 

#importing dataset
data = pd.read_csv('data/diabetic_data.csv')
#looking at each column for any data types that may need changing to help with analysis
data.columns
data.dtypes
df = data

#dropping all Columns not involved in analysis (wight, payercode)
# see DD for reason why
data = data.drop(columns=['weight','payer_code'])

#race 
#Assigned each distinct value with a numerical value (See DD for changes)
#Categorical-nominal
race_list = {'?': 0, 'AfricanAmerican': 1, 
             'Asain': 2,
             'Caucasian': 3,
             'Hispanic': 4,
             'Other': 5}
data['race'] = data['race'].map(race_list)
print(data.race)

#gender
#Assigned Female/Male Unknown/invalid as 0,1,2 respectfully, since invalid would be useful for analysis
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
            'Endocrinology/Trauma': 10,
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
            'Perintatology': 43,
            'PhysicalMedicineandRehabilitation': 44,
            'PhysicianNotFound': 45,
            'Podiatry': 46,
            'Proctology': 47,
            'Psychiatry': 48,
            'Psychiatry-Addictive': 49,
            'Psychiatry-Child/Adolescent': 50,
            'Psychology': 51,
            'Pulmonolgy': 52,
            'Radiologist': 53,
            'Radiology': 54,
            'Resident': 55,
            'Rheumatology': 56,
            'Speech': 57,
            'SportsMediicine': 58,
            'Surgeon': 59,
            'Surgery Cardiovascular': 60,
            'Surgery-Cardiovascular': 61,
            'Surgery-Colon&Rectal': 62,
            'Surgery-General': 63,
            'Surgery-Maxillofacial': 64,
            'Surgery-Neruo': 65,
            'Surgery-Pediatric': 66,
            'Surgery-Plastic': 67,
            'Surgery-PlasticwithinHeadandNeck': 68,
            'Surgery-Thoracic': 69,
            'Surgery-Vascular': 70,
            'SurgerySpecialty': 71,
            'Urology': 72}
data['medical_specialty'] = data['medical_specialty'].map(Med_list)
print(data['medical_specialty'])

#