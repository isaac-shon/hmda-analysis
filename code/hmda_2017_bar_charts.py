import dask.dataframe as dd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import os 
os.chdir("C://Users//isaac//Desktop//Projects//hmda-analysis")

# Read the large CSV file we extracted using Dask:
df = dd.read_csv('data//hmda_2017_nationwide_all-records_labels.csv', assume_missing=True, low_memory=False)

# Bar Chart 1: Purpose of Loans
loan_purpose = df['loan_purpose_name'].value_counts().compute() # Count occurrences of each category
loan_purpose = loan_purpose.reset_index() # Convert to pandas df to plot
loan_purpose.columns = ['category', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(data=loan_purpose, y='category', x='count', color = 'blue')
plt.xlabel('Count')
plt.ylabel('Purpose of Loan')
plt.savefig('output\\loan_purpose.pdf', bbox_inches = 'tight')

# Bar Chart 2: Type of Loan Applied for:
loan_type = df['loan_type_name'].value_counts().compute()
loan_type = loan_type.reset_index()
loan_type.columns = ['category', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(data=loan_type, y = 'category', x='count', color="blue")
plt.xlabel('Count')
plt.ylabel('Loan Type')
plt.savefig('output\\loan_type.pdf', bbox_inches = 'tight')

# Bar Chart 3: Financial Institution
agency = df['agency_abbr'].value_counts().compute()
agency = agency.reset_index()
agency.columns = ['category', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(data=agency, y = 'category', x='count', color="blue")
plt.xlabel('Count')
plt.ylabel('Financial Institution')
plt.savefig('output\\financial_institution.pdf', bbox_inches = 'tight')

# Bar Chart 4: Action Taken by Financial Institution (for Applications w/o Preapproval Request)
no_preapproval_request = df[df['preapproval_name'] != 'Preapproval was requested']

action_taken = no_preapproval_request['action_taken_name'].value_counts().compute()
action_taken = action_taken.reset_index()
action_taken.columns = ['category', 'count']

plt.figure(figsize=(10, 6))
sns.barplot(data=action_taken, y = 'category', x='count', color="blue")
plt.xlabel('Count')
plt.ylabel('Action Taken by Financial Institution')
plt.savefig('output\\action_taken.pdf', bbox_inches = 'tight')