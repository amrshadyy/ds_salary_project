# Data Science Salary Estimator: Project Overview
* Created a tool that estimates the average salary for data scientists with a (MAE ~ $ 3k) to increase awareness for job-seekers.
* Scraped over 800 jobs from glassdoor using selenium and python.
* Data celaning and feature engineering of variables(Salary Estimate, State, Job Description,...etc).
* Built machine learning models(Linear, Lasso, RandomForest) and optimized them using GridSearchCV to attain best results.
* Productionize our model using Flask API.

## Code and Resources
**Python Version:** 3.11                                                                                                                                                                                                                         
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, flask, json, pickle                                                                                                                                                         
**For Web Framework Requirements:** ```pip install -r requirements.txt```                                                                                                                                                                        
**Instructor Github:** https://github.com/PlayingNumbers/ds_salary_proj/tree/master                                                                                                                                                             
**Scraper Article:** https://medium.com/@arjunsatishwork/making-a-glassdoor-web-scraper-with-python-and-selenium-2024-ed89ec5d3c61                                                                                                               
**Scraper Github:** https://github.com/ArjunxyzSatish/GlassdoorScraper/tree/main

## YouTube Project Walk-Through
https://www.youtube.com/playlist?list=PL2zq7klxX5ASFejJj80ob9ZAnBHdz5O1t                                                                                                                                                                 

## Web Scraping
Scraped 860 jobs with the following features:
* Job Title
* Salary Estimate
* Job Description
* Rating
* Company Name
* Location
* Size
* Year Founded
* Type of Ownership
* Industry
* Sector
* Revenue

## Data Cleaning
Following the scraping process, the data is cleaned to be usable for exploratory analysis and model building. The following changes were made:
* Parsing numeric data out of salary
* Made columns[hourly,yearly] to differentiate between salary and hourly wage
* Removed rows with no salary given
* Made a new column for state of each company
* Transformed the founded date into company age
* Made columns for if different skills were listed in the job description:
   * Python
   * R
   * Spark
   * AWS
   * Excel

## EDA
* Feature engineering for some attributes that were not transformed during data cleaning
 * Made columns for simplified job title and seniority level
 * Made column for description length
* Plotted histograms, box plots and correlation plots for numerical data
* Made bar charts for categorical data
* Pivot tables were made to compare average salary to different categories accordingly







