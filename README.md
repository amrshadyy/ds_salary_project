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
* Type of ownership
* Industry
* Sector
* Revenue




