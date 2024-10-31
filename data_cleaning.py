# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 15:25:20 2024

@author: Lenovo (Amr Shady)
"""

import pandas as pd
df = pd.read_csv('glassdoor_scraping.csv')
print(df)

#Salary Parsing

df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if '/hr' in x.lower() else 0)
df['yearly'] = df['Salary Estimate'].apply(lambda x: 1 if '/yr' in x.lower() else 0)

df = df[df['Salary Estimate'] != 'Not listed']
minus_Kd = df['Salary Estimate'].apply(lambda x: x.replace('K', '').replace('$',''))
minus_hr_yr = minus_Kd.apply(lambda x: float(x.lower().replace('/hr','').replace('/yr','')))
df['Average Salary'] = minus_hr_yr

#State Field

df['job_state'] = df['Location'].apply(lambda x: x.split(',')[1].strip() if ',' in x else x)
df.job_state.value_counts()

#Age Field
df['Founded'] = pd.to_numeric(df['Founded'], errors = 'coerce')
df['age'] = df['Founded'].apply(lambda x: x if pd.isna(x) or x < 1 else 2024 - x) 

#Parsing of Job Description(python, etc.)

#python
df['python_yn'] = df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)

#r studio
df['R_yn'] = df['Job Description'].apply(lambda x: 1 if 'r studio' in x.lower() or 'r-studio'  in x.lower() in x.lower() else 0)

#spark
df['spark_yn'] = df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)

#aws
df['aws_yn'] = df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)

#excel
df['excel_yn'] = df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)

df.to_csv('salary_data_cleaned.csv', index= False)



