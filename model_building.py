# -*- coding: utf-8 -*-
"""
Created on Thu Oct 31 17:10:19 2024

@author: Lenovo
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('eda_data.csv')

# Fill NaN with -1
df.fillna(-1, inplace=True)

# choose relevant columns
df.columns

df_model = df[['Average Salary','Rating','Size','Type of ownership','Industry','Sector',
               'Revenue','hourly','job_state','age','python_yn','spark_yn','aws_yn',
               'excel_yn','job_simplified','seniority','desc_length']]

# get dummy data
df_dummy = pd.get_dummies(df_model, dtype=int)

# train test split
from sklearn.model_selection import train_test_split

X= df_dummy.drop('Average Salary' , axis = 1).dropna()
y= df_dummy['Average Salary'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# multiple linear regression
import statsmodels.api as sm

X_sm = X = sm.add_constant(X)
model = sm.OLS(y, X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train,y_train)

np.mean(cross_val_score(lm, X_train, y_train, scoring = 'neg_mean_absolute_error'))

# lasso regression
lm_l = Lasso(alpha=0.01)
lm_l.fit(X_train,y_train)
np.mean(cross_val_score(lm_l, X_train, y_train, scoring = 'neg_mean_absolute_error'))

alpha = []
error = []

for i in range(1,100):
    alpha.append(i/100)
    lml = Lasso(alpha = (i/100))
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring = 'neg_mean_absolute_error')))

plt.plot(alpha, error)

err = tuple(zip(alpha,error))
df_err = pd.DataFrame(err, columns = ['alpha','error'])
df_err[df_err.error == max(df_err.error)]

# random forest
from sklearn.ensemble import RandomForestRegressor
rf = RandomForestRegressor()

np.mean(cross_val_score(rf, X_train, y_train, scoring = 'neg_mean_absolute_error'))

# tune models GridsearchCV
from sklearn.model_selection import GridSearchCV
parameters = {'n_estimators':range(10,300,10), 'criterion':('squared_error','absolute_error'),
              'max_features':(1.0,'sqrt','log2')}

gs = GridSearchCV(rf,parameters,scoring= 'neg_mean_absolute_error' )
gs.fit(X_train,y_train)
gs.best_score_
gs.best_estimator_

# test ensembles
tpred_lm = lm.predict(X_test)
tpred_lml = lm_l.predict(X_test)
tpred_rf = gs.best_estimator_.predict(X_test)

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test,tpred_lm)
mean_absolute_error(y_test,tpred_lml)
mean_absolute_error(y_test,tpred_rf)

mean_absolute_error(y_test,(tpred_lm+tpred_rf)/2)

import pickle
pickl = {'model': gs.best_estimator_}
pickle.dump( pickl, open( 'model_file' + ".p", "wb" ) )

file_name = "model_file.p"
with open(file_name, 'rb') as pickled:
    data = pickle.load(pickled)
    model = data['model']
    
model.predict(X_test.iloc[1,:].values.reshape(1,-1))

list(X_test.iloc[1,:])

model.predict(X_test.iloc[[1]])

