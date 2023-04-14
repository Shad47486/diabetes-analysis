import pandas as pd   # data processing, CSV file I/O (e.g. pd.read_csv)
import numpy as np   # linear algebra
import matplotlib.pyplot as plt  #graphs and plots
from scipy import stats
import seaborn as sns   #data visualizations 
import csv # Some extra functionalities for csv  files - reading it as a dictionary
from lightgbm import LGBMClassifier #sklearn is for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction
from sklearn.model_selection import train_test_split, cross_validate   #break up dataset into train and test sets
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# importing python library for working with missing data
import missingno as msno
# To install missingno use: !pip install missingno
import re    # This library is used to perform regex pattern matching
import nbformat 
# import various functions from sklearn
from sklearn.linear_model import LogisticRegression, LinearRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import LinearSVC
from sklearn.ensemble import GradientBoostingClassifier
from catboost import CatBoostClassifier
import xgboost as xgb
from sklearn.metrics import roc_auc_score, accuracy_score, precision_score, recall_score, classification_report, make_scorer
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split
from sklearn.model_selection import KFold,cross_val_score, RepeatedStratifiedKFold,StratifiedKFold
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.preprocessing import OneHotEncoder,StandardScaler,PowerTransformer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import KNNImputer,SimpleImputer
from sklearn.compose import make_column_transformer
from imblearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.impute import SimpleImputer
from sklearn.dummy import DummyClassifier
from imblearn.over_sampling import SMOTE
from sklearn.neighbors import KNeighborsClassifier
import plotly 
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as py
from plotly.offline import iplot
from plotly.subplots import make_subplots
import plotly.figure_factory as ff
import warnings
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScale
warnings.filterwarnings("ignore")
#upload the csv and declare its name to = the csv
#for this course we will name the dataframe 'stroke', but you can change it to df or anything else you want.
#Find the file path to the .csv
#Then use code below to read .csv
diabetes = pd.read_csv('C:/Users/Shad/.pyenv/PProjects/diabetes-analysis/data/cleandata.csv')
# problem with these imports
# from sklearn.metrics import confusion_matrix, accuracy_score, balanced_accuracy_score,\
#                             precision_score, recall_score, roc_auc_score,\
#                             plot_confusion_matrix, classification_report, plot_roc_curve, f1_score

# Step 1: Select relevant columns
features = ['age', 'gender', 'time_in_hospital', 'diag_1', 'diag_2', 'diag_3', 'num_medications', 'readmitted']

# Step 2: Data preprocessing
# Handle missing values
diabetes_clean = diabetes[features].dropna()
# Scale numerical features
num_cols = ['age', 'gender', 'time_in_hospital', 'num_medications']
scaler = StandardScaler()
diabetes_clean[num_cols] = scaler.fit_transform(diabetes_clean[num_cols])
# One-hot encode categorical features
cat_cols = ['diag_1', 'diag_2', 'diag_3', 'readmitted']
diabetes_encoded = pd.get_dummies(diabetes_clean, columns=cat_cols)

# Step 3: Apply k-means clustering
k = 4  # number of clusters
kmeans = KMeans(n_clusters=k, random_state=42)
cluster_labels = kmeans.fit_predict(diabetes_encoded)
diabetes_encoded['cluster'] = cluster_labels

# Step 4: Evaluate clustering performance
silhouette_score = silhouette_score(diabetes_encoded.drop('cluster', axis=1), cluster_labels)
print(f"Silhouette score: {silhouette_score}")

wss = kmeans.inertia_
print(f"Within-cluster sum of squares: {wss}")

# Step 5: Visualize clustering results
fig, ax = plt.subplots(figsize=(10,6))
scatter = ax.scatter(diabetes_encoded['age'], diabetes_encoded['num_medications'], c=cluster_labels, alpha=0.8)
plt.legend(*scatter.legend_elements(), title='Cluster')
ax.set_xlabel('Age')
ax.set_ylabel('Number of Medications')
ax.set_title('K-Means Clustering')
plt.show()
