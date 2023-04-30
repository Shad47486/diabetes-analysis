import pandas as pd
import numpy as np 

#importing dataset
data = pd.read_csv('C:/Users/Shad/.pyenv/PProjects/diabetes-analysis/data/diabetic_data.csv')
#looking at each column for any data types that may need changing to help with analysis
data.columns
data.dtypes

#dropping all Columns not involved in analysis (wight, payercode, examide, citoglipton)
#see DD for reason why
to_remove = [11, 13, 14, 19, 20, 21]
data = data[~data['discharge_disposition_id'].isin(to_remove)]
### removeing the not needed columns and the first row that was create
to_remove3 = ['Unknown/Invalid']
data = data[~data['gender'].isin(to_remove3)]
#droppping uneeded columns
data = data.drop(columns=['encounter_id', 'patient_nbr', 'medical_specialty', 'weight',
                          'payer_code','citoglipton', 'examide',
                          'nateglinide', 'chlorpropamide',
                          'acarbose', 'miglitol', 
                          'glyburide-metformin', 'tolazamide', 
                          'metformin-pioglitazone','metformin-rosiglitazone', 'glimepiride-pioglitazone', 
                          'glipizide-metformin', 'troglitazone', 'tolbutamide', 'acetohexamide'])
data.info()

#race 
#Assigned each distinct value with a numerical value (See DD for changes)
#Categorical-nominal
#gender
#Assigned Female/Male Unknown/invalid as 0,1,2 respectfully
#Categorical-nominal
gender_list = {'Female': 0,
               'Male': 1}
data['gender'] = data['gender'].map(gender_list)
# removed genders that were invalid since there were only 3 values that where invalid
print(data.gender)

#age
#Assigned each group as a numerical Value, for example: 0-10 = 1 and the ones going on 90-100 = 10
age_list = {'[0-10)': '<30', 
            '[10-20)': '<30', 
            '[20-30)': '<30', 
            '[30-40)': '<30', 
            '[40-50)': '30-60', 
            '[50-60)': '30-60', 
            '[60-70)': '30-60', 
            '[70-80)': '60>', 
            '[80-90)': '60>', 
            '[90-100)': '60>'}
data['age'] = data['age'].map(age_list)

race_list = {'African American': 1, 
             'Asian': 2,
             'Caucasian': 3,
             'Hispanic': 4, 
             'Other': 5}
data['race'] = data['race'].map(age_list)
#medical_Speciality
#Assigned Each distinct value as a numerical number based on alphabetical order
#Med_list = {'?': 0,
#'AllergyandImmunology': 1,
#'Anesthesiology': 2,
#'Anesthesiology-Pediatric': 3,
#'Cardiology': 4,
#'Cardiology-Pediatric': 5,
#'DCPTEAM': 6,
#'Dentistry': 7,
#'Dermatology': 8,
#'Emergency/Trauma': 9,
#'Endocrinology': 10,
#'Endocrinology-Metabolism': 11,
#'Family/GeneralPractice': 12,
#'Gastroenterology': 13,
#'Gynecology': 14,
#'Hematology': 15,
#'Hematology/Oncology': 16,
#'Hospitalist': 17,
#'InfectiousDiseases': 18,
#'InternalMedicine': 19,
#'Nephrology': 20,
#'Neurology': 21,
#'Neurophysiology': 22,
#'Obsterics&Gynecology-GynecologicOnco': 23,
#'Obstetrics': 24,
#'ObstetricsandGynecology': 25,
#'Oncology': 26,
#'Ophthalmology': 27,
#'Orthopedics': 28,
#'Orthopedics-Reconstructive': 29,
#'Osteopath': 30,
#'Otolaryngology': 31,
#'OutreachServices': 32,
#'Pathology': 33,
#'Pediatrics': 34,
#'Pediatrics-AllergyandImmunology': 35,
#'Pediatrics-CriticalCare': 36,
#'Pediatrics-EmergencyMedicine': 37,
#'Pediatrics-Endocrinology': 38,
#'Pediatrics-Hematology-Oncology': 39,
#'Pediatrics-InfectiousDiseases': 40,
#'Pediatrics-Neurology': 41,
#'Pediatrics-Pulmonology': 42,
#'Perinatology': 43,
#'PhysicalMedicineandRehabilitation': 44,
#'PhysicianNotFound': 45,
#'Podiatry': 46,
#'Proctology': 47,
#'Psychiatry': 48,
#'Psychiatry-Addictive': 49,
#'Psychiatry-Child/Adolescent': 50,
#'Psychology': 51,
#'Pulmonology': 52,
#'Radiologist': 53,
#'Radiology': 54,
#'Resident': 55,
#'Rheumatology': 56,
#'Speech': 57,
#'SportsMedicine': 58,
#'Surgeon': 59,
#'Surgery-Cardiovascular': 60,
#'Surgery-Cardiovascular/Thoracic': 61,
#'Surgery-Colon&Rectal': 62,
#'Surgery-General': 63,
#'Surgery-Maxillofacial': 64,
#'Surgery-Neuro': 65,
#'Surgery-Pediatric': 66,
#'Surgery-Plastic': 67,
#'Surgery-PlasticwithinHeadandNeck': 68,
#'Surgery-Thoracic': 69,
#'Surgery-Vascular': 70,
#'SurgicalSpecialty': 71,
#'Urology': 72}
#data['medical_specialty'] = data['medical_specialty'].map(Med_list)
#print(data['medical_specialty'])

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
            'Norm': 5, 
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
readmitted_list = {'NO': 0, '>30': 0, '<30': 1}
data['readmitted'] = data['readmitted'].map(readmitted_list)

readmitted_list = {'NO': "Not Readmitted", '>30': "Not Readmitted", '<30': "Readmitted"}
data['readmitted'] = data['readmitted'].map(readmitted_list)


#looking to see if fields are in the correct data type
data.info()
#changed a1c into int after being float
data['A1Cresult'] = data['A1Cresult'].astype(int)
data['A1Cresult'] = data['A1Cresult'].astype('int64')

#diagnosis code
#Encoding the data,
def map_now():
    listname = [('infections', 139),
                ('neoplasms', (239 - 139)),
                ('endocrine', (279 - 239)),
                ('blood', (289 - 279)),
                ('mental', (319 - 289)),
                ('nervous', (359 - 319)),
                ('sense', (389 - 359)),
                ('circulatory', (459-389)),
                ('respiratory', (519-459)),
                ('digestive', (579 - 519)),
                ('genitourinary', (629 - 579)),
                ('pregnancy', (679 - 629)),
                ('skin', (709 - 679)),
                ('musculoskeletal', (739 - 709)),
                ('congenital', (759 - 739)),
                ('perinatal', (779 - 759)),
                ('ill-defined', (799 - 779)),
                ('injury', (999 - 799))]
    
    
    dictcout = {}
    count = 1
    for name, num in listname:
        for i in range(num):
            dictcout.update({str(count): name})  
            count += 1
    return dictcout
  

def codemap(data, codes):
    import pandas as pd
    namecol = data.columns.tolist()
    for col in namecol:
        temp = [] 
        for num in data[col]:           
            if ((num is None) | (num in ['unknown', '?']) | (pd.isnull(num))): temp.append('unknown')
            elif(num.upper()[0] == 'V'): temp.append('supplemental')
            elif(num.upper()[0] == 'E'): temp.append('injury')
            else: 
                lkup = num.split('.')[0]
                temp.append(codes[lkup])           
        data.loc[:, col] = temp               
    return data 


listcol = ['diag_1', 'diag_2', 'diag_3']
codes = map_now()
data[listcol] = codemap(data[listcol], codes)

data.head()



#saves data
#data.to_csv('C:/Users/Shad/.pyenv/PProjects/diabetes-analysis/data/cleandata.csv')
#not including the medical specilaties 
data.to_csv('C:/Users/Shad/.pyenv/PProjects/diabetes-analysis/data/cleandatav2.csv')
#data.to_csv('C:/Users/Shad/.pyenv/PProjects/diabetes-analysis/data/cleandatav3.csv')