import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Lenovo/Documents/ds_salary_project/chromedriver.exe"
df= gs.get_jobs('data scientist', 1000, False, path, 15)

df.to_csv('glassdoor_scraping.csv', index=False)
print(df)